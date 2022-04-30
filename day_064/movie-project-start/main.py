import sys

sys.path.insert(0, "./../..")

import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from personal_config import my_info as cfg
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

tmdb_api_key = cfg["tmdb_api"]
print(tmdb_api_key)


class Movie(db.Model):
    """Movie class for SQLAlchemy use (DB)"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(250))

    def __repr__(self):
        return "<Movie %r>" % self.id


# create the database and the table
db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )

# db.session.add(new_movie)
# db.session.commit()


class MovieEditForm(FlaskForm):
    rating = FloatField("Your rating out of 10 eg 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")


class MovieAddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    movie_to_update = db.session.query(Movie).get(movie_id)
    form = MovieEditForm()
    if form.validate_on_submit():
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_update)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.session.query(Movie).get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieAddForm()
    if form.validate_on_submit():
        movie_to_add_title = form.title.data
        print(movie_to_add_title)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
