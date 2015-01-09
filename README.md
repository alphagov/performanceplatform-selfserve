# Performance Platform self-serve prototype

[http://selfserve.herokuapp.com/](http://selfserve.herokuapp.com/)

## Setup

`npm install`

`npm install -g gulp`

`pip install -r requirements.txt`

Alternatively, you can install into a virtualenv. Virtualenv provides a way to keep different project environments isolated.

To get started, run:

`sudo pip install virtualenv`

`virtualenv venv`

`. venv/bin/activate`

`pip install -r requirements.txt`

## SASS compilation

`gulp watch`

It will recompile the SASS every time a file changes.

## Running

`python manage.py runserver`

or

`foreman start`

The app will run at [http://localhost:8000](http://localhost:8000)

## Heroku

`heroku git:remote -a selfserve`

`heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-python`

`git push heroku master`
