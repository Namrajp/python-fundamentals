from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/hi')
def hi():
    return "Hi!"

@app.route('/bye')
def bye():
    return "Bye!"
