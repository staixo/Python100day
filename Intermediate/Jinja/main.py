from flask import Flask, render_template
import random
import datetime
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    footer = "Copyright " + str(datetime.date.today().year) + " Henri "
    return render_template('index.html', num=random_number, footer=footer, name=None,gender=None,age=None)


@app.route('/guess/<name>')
def guess(name):
    random_number = random.randint(1, 10)
    # get gender
    genderurl = f"http://api.genderize.io?name={name}"
    genderresponse = requests.get(genderurl, verify=False).json()
    gender = genderresponse.get('gender')
    #get age
    age = f"http://api.agify.io?name={name}"
    ageresponse = requests.get(age, verify=False).json()
    age = ageresponse.get('age')
    # footer
    footer = "Copyright " + str(datetime.date.today().year) + " Henri "
    return render_template('index.html', num=random_number, footer=footer, name=name, gender=gender,age=age)


if __name__ == "__main__":
    app.run(debug=True)
