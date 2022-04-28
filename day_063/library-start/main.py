from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    """Book class for SQLAlchemy use (DB)"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Book %r>" % self.id


# create the database and the table
db.create_all()


@app.route("/")
def home():
    # Challenge 1
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # Challenge 2
    if request.method == "POST":
        # convert book management from dict to Book object
        book = Book(
            title=request.form.get("book"),
            author=request.form.get("author"),
            rating=request.form.get("rating"),
        )
        # book_dict = {
        #     "title": request.form.get("book"),
        #     "author": request.form.get("author"),
        #     "rating": request.form.get("rating"),
        # }
        # all_books.append(book_dict)
        db.session.add(book)
        db.session.commit()

        all_books = db.session.query(Book).all()
        print(all_books)
        return render_template("index.html", books=all_books)
    return render_template("add.html")


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    """Add edit rating function to the app"""
    book = db.session.query(Book).get(book_id)
    if request.method == "POST":
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form.get("rating")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)


@app.route("/delete/<book_id>")
def delete(book_id):
    """Add delete function to the app"""
    book_to_delete = db.session.query(Book).get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
