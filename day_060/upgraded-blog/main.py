import smtplib

import requests
from flask import Flask, render_template, url_for, request

import sys

sys.path.insert(0, "./../..")
from personal_config import my_info as cfg

user_info = cfg.get("yahoo_mail")
my_email = user_info.get("email")
password = user_info.get("password")
smpt_setting = user_info.get("smtp")
port = user_info.get("port")
to_email = cfg.get("gmail_mail").get("email")

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()


def send_mail(username, email_addr, phone_num, message_to_send):
    with smtplib.SMTP(host=smpt_setting, port=port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        header = f"To: {to_email}\nFrom: {my_email}\nSubject: Contact Form Submission\n\n"
        msg = (
            header
            + f"New message received!\n\nName: {username}\nEmail: {email_addr}\nPhone Number: {phone_num}\nMessage: {message_to_send}"
        )
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # print(request.form["name"])
        # print(request.form["email"])
        # print(request.form["phone"])
        # print(request.form["message"])
        send_mail(
            request.form["name"], request.form["email"], request.form["phone"], request.form["message"]
        )
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
