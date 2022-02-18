import smtplib
import sys
import time
from datetime import datetime, timezone

import requests

sys.path.insert(0, "../../")

from personal_config import my_info

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude
MY_LAT = my_info["my_location"]["lat"]
MY_LONG = my_info["my_location"]["lng"]

from_info = my_info["yahoo_mail"]
from_email = from_info["email"]
from_password = from_info["password"]
from_smtp = from_info["smtp"]
from_port = from_info["port"]

to_info = my_info["gmail_mail"]
to_email = to_info["email"]


def iss_close_to_me():
    """return true of iss latitude and longtidue are close to my location (within 5 degrees)"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def dark_now(sunrise_hour, sunset_hour):
    """return true if it is dark now"""
    time_now = datetime.now(timezone.utc).hour
    # return not (time_now > sunrise_hour and time_now < sunset_hour)
    return time_now > sunset_hour or time_now < sunrise_hour


def send_mail():
    """send email to my gmail account"""
    with smtplib.SMTP(host=from_smtp, port=from_port) as connection:
        connection.starttls()
        connection.login(from_email, from_password)
        header = f"From: {from_email}\nTo: {to_email}\nSubject: Look up👆\n\n"
        msg = header + "Now is the perfect time to look up, the ISS is over your head!"
        connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=msg)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if iss_close_to_me() and dark_now(sunrise, sunset):
        print("True")
        send_mail()
    print("False")
    time.sleep(60)
