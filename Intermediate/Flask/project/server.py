from flask import Flask
from flask import render_template


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
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
