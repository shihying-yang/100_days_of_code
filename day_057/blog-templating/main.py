from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<post_id>")
def get_post(post_id):
    print(type(post_id))
    for post in all_posts:
        if str(post["id"]) == post_id:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
