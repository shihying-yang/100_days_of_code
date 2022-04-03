import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello World!"
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    correct_name = name.title()
    res1 = requests.get(f"https://api.genderize.io?name={name}")
    retrieved_gender = res1.json().get("gender")
    res2 = requests.get(f"https://api.agify.io?name={name}")
    retrieved_age = res2.json().get("age")
    return render_template("guess.html", name=correct_name, age=retrieved_age, gender=retrieved_gender)


if __name__ == "__main__":
    app.run(debug=True)
