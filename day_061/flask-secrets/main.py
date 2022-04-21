from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# from wtforms.validators import DataRequired

app = Flask(__name__)

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
    login_form.validate_on_submit()
    # if form.validate_on_submit():
    #     return render_template("success.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
