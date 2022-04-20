import requests
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        return f"<h1>Successfully sent your message!</h1>"
    else:
        return render_template("contact.html")

@app.route("/post/<post_id>")
def get_post(post_id):
    for post in all_posts:
        if str(post["id"]) == post_id:
            return render_template("post.html", post=post)
        
# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     # return f"<h1>test</h1>"
#     if request.method == "POST":
#         # print("blah")
#         # print(request.form["name"])
#         # print(request.form["email"])
#         # print(request.form["phone"])
#         # print(request.form["message"])
#         return f"<h1>{request.form['name']}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
