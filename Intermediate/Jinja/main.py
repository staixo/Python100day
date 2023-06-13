from flask import Flask
import jinja2
from flask import render_template
import random
import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    footer = "Copyright " + str(datetime.date.today().year) + " Henri "
    return render_template('index.html',num=random_number,footer=footer)


if __name__ == "__main__":
    app.run(debug=True)
