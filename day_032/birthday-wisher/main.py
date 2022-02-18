##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


from calendar import c
import datetime as dt
import random
import smtplib
import sys

sys.path.insert(0, "./../..")

import pandas as pd
from personal_config import my_info as cfg

# setup the from email account
user_info = cfg.get("yahoo_mail")
my_email = user_info.get("email")
password = user_info.get("password")
smpt_setting = user_info.get("smtp")
port = user_info.get("port")


bdays_df = pd.read_csv("birthdays.csv")
bdays_list = bdays_df.to_dict(orient="records")

now = dt.datetime.now()
today_m = now.month
today_day = now.day
# print(f"today_m: {type(today_m)} today_day: {type(today_day)}")


def get_random_letter():
    """select a random letter from the letter templates"""
    template_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{template_num}.txt", "r") as letter_template:
        content = letter_template.read()
    return content


# 4. Send the letter generated in step 3 to that person's email address.
def send_birthday_mail(to_person, letter_content):
    """send happy birthday email to a person"""
    with smtplib.SMTP(host=smpt_setting, port=port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        header = f"To: {to_person.get('email')}\nFrom: {my_email}\nSubject: Happy Birthday!\n\n"
        # replace the [NAME] with the person's actual name from birthdays.csv
        msg = header + letter_content.replace("[NAME]", to_person.get("name"))
        connection.sendmail(from_addr=my_email, to_addrs=to_person.get("email"), msg=msg)


# 2. Check if today matches a birthday in the birthdays.csv
for person in bdays_list:
    person_m = person["month"]
    person_day = person["day"]
    # print(type(person_m), type(person_day))
    if person_m == today_m and person_day == today_day:
        # 3. If step 2 is true, pick a random letter from letter templates
        email_content = get_random_letter()
        send_birthday_mail(person, email_content)
    else:
        continue


# ## Angela's way is to use pandas iterrows(), and it looks like this:
# today = dt.datetime.now()
# today_tuple = (today.month, today.day)

# data = pd.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     pass
