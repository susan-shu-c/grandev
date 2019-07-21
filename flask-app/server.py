import os

from numpy import stack
from imageio import imread
from keras.models import load_model
from keras.models import model_from_json
import json
from PIL import Image
from flask import (Flask, flash, render_template, redirect, request, session,
                   send_file, url_for)
from werkzeug.utils import secure_filename
import cv2

from utils import (is_allowed_file, generate_barplot, generate_random_name,
                   make_thumbnail)

MODEL_PATH = os.environ['NEURAL_NET_MODEL_PATH'] # the .json file TODO: Change variable names
WEIGHTS_PATH = os.environ['NEURAL_NET_WEIGHTS_PATH'] # the .h5 file

with open(MODEL_PATH,'r') as f:
    model_json = json.load(f)

CLASSINATOR = model_from_json(model_json) # the model architecture as read from .json
CLASSINATOR.load_weights(WEIGHTS_PATH) # Load weights from .h5 into the model
CLASSINATOR._make_predict_function() 
    # as suggested attempt to fix bug with `model._make_predict_function()`

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['UPLOAD_FOLDER'] = os.environ['UPLOAD_FOLDER']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # show the upload form
        return render_template('home.html')

    if request.method == 'POST':
        # check if a file was passed into the POST request
        if 'image' not in request.files:
            flash('No file was uploaded.')
            return redirect(request.url)

        image_file = request.files['image']

        # if filename is empty, then assume no upload
        if image_file.filename == '':
            flash('No file was uploaded.')
            return redirect(request.url)

        # check if the file is "legit"
        if image_file and is_allowed_file(image_file.filename):
            filename = secure_filename(generate_random_name(image_file.filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)
            # HACK: Defer this to celery, might take time
            passed = make_thumbnail(filepath)
            if passed:
                return redirect(url_for('predict', filename=filename))
            else:
                return redirect(request.url)


@app.errorhandler(500)
def server_error(error):
    """ Server error page handler """
    return render_template('error.html'), 500


@app.route('/images/<filename>')
def images(filename):
    """ Route for serving uploaded images """
    if is_allowed_file(filename):
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        flash("File extension not allowed.")
        return redirect(url_for('home'))


@app.route('/predict/<filename>')
def predict(filename):
    """ After uploading the image, show the prediction of the uploaded image
    in barchart form
    """
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image_url = url_for('images', filename=filename)
    image_mtx = imread(image_path)
    # image_mtx = image_mtx.astype(float) / 255.

    image_mtx = cv2.resize(image_mtx, (150, 150), interpolation=cv2.INTER_CUBIC)
    image_mtx = image_mtx / 255.

    try:
        # HACK: imageio seems to automatically infer grayscale images as a
        # 2d tensor, not 3d; need to support this logic. For now just duplicate
        # the first channel.
        image_mtx = image_mtx[:, :, :3]
    except IndexError:
        image_mtx = stack((image_mtx, image_mtx, image_mtx), axis=2)

    # image_mtx = image_mtx.reshape(-1, 128, 128, 3)
    # TODO: Celery defer this as it may take some time

    
    predictions = CLASSINATOR.predict(image_mtx.reshape(-1, 150, 150, 3))
    # TODO: Barplots with hover functionality
    script, div = generate_barplot(predictions)

    return render_template(
        'predict.html',
        plot_script=script,
        plot_div=div,
        image_url=image_url
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
