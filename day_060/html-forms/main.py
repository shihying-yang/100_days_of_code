from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    # print("triggered")
    if request.method == "POST":
        name = request.form["username"]
        pswd = request.form["password"]
        print(name, pswd)
        return render_template("user.html", username = name, password=pswd)


if __name__ == "__main__":
    app.run(debug=True)
