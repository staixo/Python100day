from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []


class addbook(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')
from flask import Flask, render_template, request, redirect, url_for



@app.route('/')
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = addbook()
    if form.validate_on_submit():
        new_book = {
            "title": form.data["title"],
            "author": form.data["author"],
            "rating": form.data["rating"]
        }
        all_books.append(new_book)
        print(all_books)
        
        #NOTE: You can use the redirect method from flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
      
    return render_template("add.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)