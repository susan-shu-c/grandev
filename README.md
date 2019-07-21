# grandev

This project is a web app that allows the user to upload an image, which the trained neural network will output whether the image is of the American singer, Ariana Grande.

## Contents
1. Web scraper for training data
2. Neural network training with Keras
3. Flask web app deployment

## Web scraper for training data
* `imagespider`: one crawler for Ariana images, one for non-Ariana images.

## Neural network training with Keras
* Uses Keras `ImageDataGenerator` to perform data augumentation.
* `model_training.ipynb` uses a vanilla model (from Andrew Ng), utilizing the `.hdf5` dataset input format.
* `model_training_keras_scratch.ipynb` trains on a basic architecture found on the Keras documentation (see reference links below).
* After training, output the model architecture as `.json` and the weights as `.h5`

## Flask web app deployment
* Use Flask to generate default UI (see reference links below).
* Allow for user to upload images, which are resized.
* Load the model architecture and weights into the web app.
* Call `.predict()` and output the result accordingly.

## Reference links
* Flask app portion: https://stackschool.io/quick-image-classifier-web-application-with-flask-keras-and-bokeh/
* Keras documentation: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
* Flask quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/
