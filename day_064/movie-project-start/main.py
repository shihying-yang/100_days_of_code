import sys
from urllib import response

sys.path.insert(0, "./../..")

import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from personal_config import my_info as cfg
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

# Flask app and bootstrap
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

tmdb_api_key = cfg["tmdb_api"]
tmdb_url = "https://api.themoviedb.org/3"


class Movie(db.Model):
    """Movie class for DB with SQLAlchemy"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(250))

    def __repr__(self):
        return "<Movie %r>" % self.id


# create the database and the table
db.create_all()

## Demo movie
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
    """Edit Movie rating and review form"""

    rating = FloatField("Your rating out of 10 eg 7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")


class MovieAddForm(FlaskForm):
    """Search movie by title form"""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


def get_movies_from_title(movie_name):
    """Call TMDB with movie title and return list of movies"""
    URL = f"{tmdb_url}/search/movie?api_key={tmdb_api_key}&query={movie_name}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    return data.get("results")


def get_movie_detail(movie_id):
    """Call TMDB with movie id and return movie details"""
    URL = f"{tmdb_url}/movie/{movie_id}?api_key={tmdb_api_key}"
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    return data


def add_movie_ranking(movie_list):
    """Add movie rankings based on the movie list"""
    for ind, movie in enumerate(movie_list):
        movie.ranking = len(movie_list) - ind
    db.session.commit()


@app.route("/")
def home():
    ## Original movie lists wihtout sorting
    # all_movies = db.session.query(Movie).all()
    # Sort movies by rating
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    # rearrange ranking to movies
    add_movie_ranking(all_movies)
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit movie rating and review in the db"""
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
    """delete movie from db"""
    movie_id = request.args.get("id")
    movie_to_delete = db.session.query(Movie).get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """find movie by title and add to db"""
    form = MovieAddForm()
    if form.validate_on_submit():
        movie_to_add_title = form.title.data
        movies = get_movies_from_title(movie_to_add_title)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select_movie():
    movie_id = request.args.get("id")
    movie_detail = get_movie_detail(movie_id)
    movie = Movie(
        title=movie_detail["title"],
        year=movie_detail["release_date"][:4],
        description=movie_detail["overview"],
        review="",
        img_url=f'https://image.tmdb.org/t/p/w500{movie_detail["poster_path"]}',
    )
    db.session.add(movie)
    db.session.commit()
    id = db.session.query(Movie).filter_by(title=movie_detail["title"]).first().id
    return redirect(url_for("edit", id=id))


if __name__ == "__main__":
    app.run(debug=True)
