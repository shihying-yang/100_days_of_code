from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#  Manager Login with Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # return User.get_id(user_id)
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


def hash_password(password):
    """use generate_password_hash to create password hash to store in the database"""
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)


@app.route("/")
def home():
    print(hash_password("yang2580"))
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=hash_password(request.form["password"]),
        )
        db.session.add(new_user)
        db.session.commit()
        # login and authenticate user
        login_user(new_user)

        return render_template("secrets.html", user=new_user.name)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=request.form["email"]).first()
        # if hash_password(request.form["password"]) == user.password:
        if check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("secrets", user=user.name))
        else:
            return "<h1>Wrong Password</h1>"
    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    # print(current_user.name)
    return render_template("secrets.html", user=current_user.name)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
