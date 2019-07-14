# Jul_14_2019

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
