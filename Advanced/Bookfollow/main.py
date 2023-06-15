from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        
        # NOTE: You can use the redirect method from Flask to redirect to another route 
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))
      
    return render_template("add.html", form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
