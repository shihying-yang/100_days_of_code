from flask import Flask
import random

number = random.randint(1, 9)
# print(number)

app = Flask(__name__)


@app.route("/")
def intro():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/qLRB2YK95yMpYc5HZD/giphy.gif">'
    )


@app.route("/<int:guess>")
def guess(guess):
    if guess == number:
        return (
            '<h1 style="color:green">You got it!</h1>'
            '<img src="https://media.giphy.com/media/l2Sqir5ZxfoS27EvS/giphy.gif">'
        )
    elif guess > number:
        return (
            '<h1 style="color:red">Too high! Try again.</h1>'
            '<img src="https://media.giphy.com/media/VWwS82FgMKRm8/giphy.gif">'
        )
    else:
        return (
            '<h1 style="color:purple">Too low! Try again.</h1>'
            '<img src="https://media.giphy.com/media/ApKWlcreFhuz6/giphy.gif">'
        )


if __name__ == "__main__":
    app.run(debug=True)
