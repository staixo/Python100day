from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import redirect
from wtforms.fields import PasswordField
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # N'oubliez pas de définir votre clé secrète

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Effectuez ici les actions nécessaires après la soumission du formulaire
        username = form.username.data
        password = form.password.data

        # Exemple : vérifier les identifiants de connexion
        if username == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')





@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)