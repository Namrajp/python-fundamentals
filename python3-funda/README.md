To run flask in this project:

- flask run

# flask run is enough because real command is : FLASK_APP=app.py flask run

- I have provided application login in app.py in Path environment using export FLASK_APP=app.py

## we need to enable debug mode when we’re working on our project and server is watching for changes.

- FLASK_APP=app.py FLASK_DEBUG=1 flask run

## To work with python environment:

$ pip install virtualenv # low level virtual environment, less prefereable to use
$ pip3 install virtualenvwrapper # high level environment with abstraction

lsvirtualenv
mkvirtualenv first-flask-app
workon first-flask-app
pip install flask
deactivate

## install dependencies

Find dependencies of a Project:
-pip list

-pip freeze

How to find a current shell is bash or zsh
-$ echo $0 -$ echo $SHELL
echo $0 is more accurate and if you type bash in zsh shell

To change prompt to include a new line PS1="$PS1\n"

Uninstall existing versions
pip uninstall werkzeug Flask-Login

Reinstall all dependencies
pip freeze > requirements.txt

pip install -r requirements.txt
