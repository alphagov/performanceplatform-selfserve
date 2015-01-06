# Performance Platform self-serve prototype

## Setup

npm install 

pip install -r requirements.txt

## SASS compilation

From /performanceplatformselfserve/static, run 'gulp watch'. It will recompile the SASS every time a file changes.

## Running

python manage.py runserver

or 

foreman start

The app will run at [http://localhost:5000](http://localhost:5000)

## Heroku

heroku git:remote -a selfserve
 
heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-python

git push heroku master

Url is [http://selfserve.herokuapp.com/](http://selfserve.herokuapp.com/)