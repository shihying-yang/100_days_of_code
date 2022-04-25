import csv

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    # Exercise:
    # add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
    # make coffee/wifi/power a select element with choice of 0 to 5.
    # e.g. You could use emojis ☕️/💪/✘/🔌
    # make all fields required except submit
    # use a validator to check that the URL field has a URL entered.
    # ---------------------------------------------------------------------------
    location = StringField("Location", validators=[URL()])
    open = StringField("Open")
    close = StringField("Close")
    coffee = SelectField("Coffee", choices=["😣", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], default="☕")
    wifi = SelectField("Wifi", choices=["❌", "📶", "📶📶", "📶📶📶", "📶📶📶📶", "📶📶📶📶📶"], default="📶")
    power = SelectField("Power", choices=["❌", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], default="🔌")

    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerow(
                [
                    form.cafe.data,
                    form.location.data,
                    form.open.data,
                    form.close.data,
                    form.coffee.data,
                    form.wifi.data,
                    form.power.data,
                ]
            )
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
