from flask import Flask
import random

toguess = random.randint(1, 100)
myguess = 0


def make_heading(func):
    def wrapper(value):
        return "<h1>" + str(func(value)) + "</h1>"
    return wrapper


def make_emphasis(func):
    def wrapper(value):
        return "<em>" + str(func(value)) + "</em>"
    return wrapper


def make_header(func):
    def wrapper(value):
        return "<h2>" + str(func(value)) + "</h2>"
    return wrapper


def make_bold(func):
    def wrapper(value):
        return "<strong>" + str(func(value)) + "</strong>"
    return wrapper


def make_underlined(func):
    def wrapper(value):
        return "<u>" + str(func(value)) + "</u>"
    return wrapper


def add_image(image_url):
    def decorator(func):
        def inner_wrapper(value=None):
            return str(func(value)) + "<br><img src='" + image_url + "'/>"
        return inner_wrapper
    return decorator


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@add_image("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")
def greet(value=None):
    return 'Hello guess the number :)' 


@app.route('/greet/<value>')
@make_bold
@make_header
def guess_number(value):
    if int(value) == toguess:
        return 'Bravo <br><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    if int(value) > toguess:
        return 'Too high <br><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    if int(value) < toguess:
        return 'Too low <br><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'


if __name__ == "__main__":
    app.run(debug=True)
