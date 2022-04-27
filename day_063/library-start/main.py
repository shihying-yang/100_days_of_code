from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Book %r>" % self.title


db.create_all()


@app.route("/")
def home():
    # Challenge 1
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # Challenge 2
    if request.method == "POST":
        book_dict = {
            "title": request.form.get("book"),
            "author": request.form.get("author"),
            "rating": request.form.get("rating"),
        }
        all_books.append(book_dict)
        return render_template("index.html", books=all_books)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
