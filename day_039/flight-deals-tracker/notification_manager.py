"""Class to handle the SMS notification"""
import sys

from twilio.rest import Client

from flight_data import FlightData

sys.path.insert(0, "../..")

from personal_config import my_info

twilio_from = my_info["twilio_from_number"]
twilio_to = my_info["twilio_to_number"]
twilio_sid = my_info["twilio_sid"]
twilio_auth = my_info["twilio_auth_token"]


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self, data: FlightData):
        """init the class with the data from FlightData class"""
        self.data = data

    def send_sms(self):
        """handles the real SMS sending mechanism"""
        client = Client(twilio_sid, twilio_auth)
        msg = f"✈ Low price alert! Only ${self.data.price} to fly from "
        msg += f"{self.data.city_from} ({self.data.fly_from}) to "
        msg += f"{self.data.city_to} ({self.data.fly_to}) from "
        msg += f"{self.data.out_date} to {self.data.in_date}."
        # print(msg)
        message = client.messages.create(
            body=msg,
            from_=twilio_from,
            to=twilio_to,
        )
        print(message.status)
        print(message.body)
