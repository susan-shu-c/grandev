# Jul_21_2019

* Create .hdf5 training dataset (works better with vanilla model)

* Got basic vanilla baseline model to work

* Now working on using Keras/Tensorflow

* Keras has different basic way of importing dataset - just put the files in diff folders (note the subdirectory structure, and need file extension .jpg)

```python
import h5py
f = h5py.File('../training_dataset.hdf5', 'r')
list(f.keys())
out: ['test_img', 'test_labels', 'train_img', 'train_labels']
import matplotlib.pylab as plb
```



# Jul_14_2019

> TODO: figure out how to package my own trained model and load it.

See: https://machinelearningmastery.com/save-load-keras-deep-learning-models/

* Got the image upload to work!

## Load a model
```python
from imageio import imread
import cv2

from keras.models import load_model
from keras.models import model_from_json
import json

with open('classinator_archi_v0.json','r') as f:
    model_json = json.load(f)

model = model_from_json(model_json)
model.load_weights('/home/susan/Documents/Projects/grandev/flask-app/model_temp/classinator_v0.h5')
image = imread('/home/susan/Documents/Projects/grandev/flask-app/test_upload.jpg')

image = cv2.resize(image, (150, 150), interpolation=cv2.INTER_CUBIC)
image = image / 255. # normalize pixels to between 0 and 1 as this is how model was originally trained
model.predict(image.reshape(-1, 150, 150, 3)) # outputs the probability of image being in each class.
```


```console
export NEURAL_NET_WEIGHTS_PATH='/home/susan/Documents/Projects/grandev/flask-app/model_temp/classinator_v0.h5'
export NEURAL_NET_MODEL_PATH='/home/susan/Documents/Projects/grandev/flask-app/model_temp/classinator_archi_v0.json'

export SECRET_KEY="placeholderkey"

export UPLOAD_FOLDER="/home/susan/Documents/Projects/grandev/flask-app/static/temp"
``` 
-- the above to pass into `server.py` arguments


`model = load_model('/home/susan/Documents/Projects/grandev/flask-app/model_temp/SouqNet128v2_gpu.h5')` # copy paste ease

## Complete guide to set up

```console
cd ~/grandev_venv/bin
source activate
cd ~/Documents/Projects/grandev/imagespider
scrapy shell [url]
```

Awkwardly forgot how to launch the virtual environment.

`whereis python3`

`cd /usr/bin/` - useless

`python3 -m venv grandev_venv`
`. grandev_venv/bin/activate`

## Virtual environment is here!!!

`cd ~/grandev_venv/bin` -- I just put it in home folder. Ignore `grandev` folder?
`source activate`
`pip3 list` -- list all packages
`scrapy crawl image_spider -o logging.json` -- default crawlling command

### Next steps

0. I have images now
1. Basic af classifier - prolly just grab a cat one to train (deal with accuracy later, the main this is an MVP to deploy)
2. Figure out deployment with Flask (Go? - **Wishlist item**, not **MVP** item)

**Stretch goals**
1. GO
2. Higher accuracy, more sophisticated architecture
3. User input on accuracy

## p 
11
111

# Jul_06_2019

Testing using scrapy shell!!! - REMEMBER TO USE VENV

```console
scrapy shell 'https://www.gettyimages.ca/photos/ariana-grande?family=editorial&phrase=ariana%20grande&sort=best#license'
```

```console
response.css('img').xpath('@src').getall()
```

# TODO: 
- SSH into GitHub

get ubuntu
https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows?_ga=2.113031757.891330654.1561860246-2033029163.1561860246#0

Create own model and "pickle" (or other method)
- https://machinelearningmastery.com/save-load-keras-deep-learning-models/

DOCKER + FLASK
https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5

image scraping
https://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/

https://github.com/sushrutt12/scrapingimages

getty images
https://github.com/sushrutt12/scrapingimages

Look up XPath tutorial

Spiders
https://docs.scrapy.org/en/latest/topics/spiders.html

Python 3.6.6

getty images
- https://www.gettyimages.ca/photos/ariana-grande?family=editorial&phrase=ariana%20grande&sort=mostpopular

virtualenv
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

comparison django/flask
- https://docs.python-guide.org/scenarios/web/

potential flask front-end
- https://realpython.com/the-ultimate-flask-front-end/

image classification - flask
- https://stackschool.io/quick-image-classifier-web-application-with-flask-keras-and-bokeh/
- https://github.com/syaffers/souqnet-app/blob/master/ARTICLE.md

image classification (possible reference code)
- https://www.analyticsvidhya.com/blog/2019/01/build-image-classification-model-10-minutes/
