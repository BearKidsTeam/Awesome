# Awesome
A simple and lightweight stuff-sharing web app.

[![Build Status](https://travis-ci.org/BearKidsTeam/Awesome.svg?branch=master)](https://travis-ci.org/BearKidsTeam/Awesome)
[![Code Climate](https://codeclimate.com/github/BearKidsTeam/Awesome/badges/gpa.svg)](https://codeclimate.com/github/BearKidsTeam/Awesome/badges)

## Notice:

_Unfinished code stuff. You can ignore this repo._  
_Unfinished code stuff. You can ignore this repo._  
_Unfinished code stuff. You can ignore this repo._


## Why do this:

The goal is build an alternaive web app for my original stuff-sharing static website.

## Deps:

- django // OF COURSE WE NEED THIS
- markdown // for parsing markdown text to html

## Setup:

- `mysite/settings.py` not provided, but it's basicly just a default generated one with `'awesome.apps.AwesomeConfig'` added to its `INSTALLED_APPS`.
- create a virtual environment with `python3 -m venv ./venv`
- restore requirements from requirements.txt `pip install -r requirements.txt`
- do migration `python3 manage.py migrate`
- run server `python3 manage.py runserver`
- done :)

## FAQ:

 - Site preview?  
 [Here you are](http://blumia.pythonanywhere.com/). I don't promise code which this site using is always the same as this repo
 - License?  
 No idea, since this site is still under construction, leave a license after it has a stable release is better
 - What you call a three humps camel?  
 I don't know
 - Seriously, Will this repo finally have a stable release?  
 I don't know. really.
