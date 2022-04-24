from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "not_a_secret"


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    login_form = LoginForm()
    email = login_form.email.data
    password = login_form.password.data
    if login_form.validate_on_submit():
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=LoginForm())


if __name__ == "__main__":
    app.run(debug=True)
