# Portfolio
A personal website to display some info about myself and some of the projects I am working on. Built using [Python 3.7.2](https://www.python.org/downloads/release/python-372/) and [Flask](http://flask.palletsprojects.com/en/1.1.x/installation/). You can check it out live [here](https://nate-lewis-portfolio-heroku.herokuapp.com/).

# Building
It is recommended to run this in a virtual environment.

To run the virtual environment use `. portfolio/bin/activate`

Install all the dependencies with `pip install -r requirements.txt`

Export the app so that Flask can see it `export FLASK_APP=server.py`

Finally run the app with `flask run`

# Deployment
I am using [Heroku](https://www.heroku.com/) to handle the deployment of my website. Because of the length of the website I am also using bit.ly to shorten my link to bit.ly/n-lewis

# [Server.py](./server.py)

## Routes

### `/`
This route renders index.html

Method: GET

### `/<page_name>`
This route is currently not accessed from the main page. However it can be used to access [components.html](./templates/components.html) file provided by the template. This need to be manually accessed.

Method: GET

### `/submit_form`
This route is used in conjunction with the contact form. It is used to send me an email notification.

Method: POST

# [index.html](./templates/index.html)
The base template is from [Mashup-Templates](http://www.mashup-template.com/) it was then modified to fit my needs.
