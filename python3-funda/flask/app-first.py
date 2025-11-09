from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello(): 
    return "Hello, World!"


@app.route('/welcome/home')
def welcome():
    return "Welcome home!"

@app.route('/welcome/back')
def back():
    return "welcome back!"
@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return str(a + b)
@app.route('/product/<int:a>/<int:b>')
def product(a, b):
    return str(a * b)   
@app.route('/sub/<int:a>/<int:b>')
def sub(a, b):
    return str(a - b)
@app.route('/div/<int:a>/<int:b>')
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return str(a / b)

@app.route('/math/<operation>/<int:a>/<int:b>')
def math(operation, a, b):
    if operation == 'add':
        return str(a + b)
    elif operation == 'subtract':
        return str(a - b)
    elif operation == 'multiply':
        return str(a * b)
    elif operation == 'divide':
        if b == 0:
            return "Error: Division by zero"
        return str(a / b)
    else:
        return "Error: Invalid operation"
    
  
@app.route('/users')
def fillInstructors():
    names_of_instructors = ["Elie", "Tim", "Matt"]
    random_name = "Tom"
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"  
@app.route('/title')
def title():
    return "WELCOME TO THE SECOND PAGE!" 

# we need a route to render the form
@app.route('/show-form')
def show_form():
    return render_template('first-form.html')

# we need to do something when the form is submitted
@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return f"You put {first} {last}"