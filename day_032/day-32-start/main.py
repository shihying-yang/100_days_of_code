import datetime as dt
import random
import smtplib
import sys

sys.path.insert(0, "./../..")

from personal_config import my_info as cfg

# setup the from email account
user_info = cfg.get("yahoo_mail")
my_email = user_info.get("email")
password = user_info.get("password")
smpt_setting = user_info.get("smtp")
port = user_info.get("port")
# setup the to email account
to_user_info = cfg.get("gmail_mail")
to_email = to_user_info.get("email")


def get_quote():
    """get a random quote from the quotes.txt file"""
    with open("quotes.txt", "r") as quote_file:
        quotes = quote_file.readlines()

    quote = random.choice(quotes)
    # quote = quote.replace("-", "\n" + "\t" * 5 + "-")
    return quote


def send_mail(from_addr, password, to_addr, smtp_setting, port, subject, message):
    """function to handle the send email"""
    with smtplib.SMTP(host=smtp_setting, port=port) as connection:
        connection.starttls()
        connection.login(from_addr, password)
        header = f"To: {to_addr}\nFrom: {from_addr}\nSubject: {subject}\n\n"
        msg = header + message
        connection.sendmail(from_addr, to_addr, msg)


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    send_mail(my_email, password, to_email, smpt_setting, port, "Monday Motivation", get_quote())


# ----------------------------------------intro----------------------------------------

# print(f"my_email: {my_email}\npassword: {password}")

# sys.exit(0)

# connection = smtplib.SMTP(host="smtp.mail.yahoo.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="ysying888@gmail.com",
#     msg="Subject:Hello\n\nHello, this is the body of my email.",
# )
# connection.close()

# with smtplib.SMTP(host=smpt_setting, port=port) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=to_email,
#         msg="Subject:Hello\n\nHello, this is the body of my email.",
#     )


# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# # print(day_of_week)
# # print(type(now))

# date_of_birth = dt.datetime(year=1976, month=7, day=28, hour=9)
# print(date_of_birth)
