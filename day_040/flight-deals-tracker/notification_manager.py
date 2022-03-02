"""Class to handle the SMS notification"""
import json
import smtplib
import sys
from webbrowser import get

import requests
from twilio.rest import Client

from data_manager import DataManager
from flight_data import FlightData

sys.path.insert(0, "../..")

from personal_config import my_info

yahoo_info = my_info["yahoo_mail"]

twilio_from = my_info["twilio_from_number"]
twilio_to = my_info["twilio_to_number"]
twilio_sid = my_info["twilio_sid"]
twilio_auth = my_info["twilio_auth_token"]

bit_url = my_info["bitly_url"]
bit_token = my_info["bitly_access_token"]


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self, data: FlightData, users_data=None):
        """init the class with the data from FlightData class"""
        self.data = data
        self.users_data = users_data

    def send_sms(self):
        """handles the real SMS sending mechanism"""
        client = Client(twilio_sid, twilio_auth)
        msg = f"✈ Low price alert! Only ${self.data.price} "
        msg += f"to fly from {self.data.city_from} ({self.data.fly_from}) "
        msg += f"to {self.data.city_to} ({self.data.fly_to}) "
        if self.data.stop_over_cities != 0:
            msg += f"via {self.data.stop_over_cities[0]} "
        msg += f"from {self.data.out_date} to {self.data.in_date}."
        # print(msg)
        message = client.messages.create(
            body=msg,
            from_=twilio_from,
            to=twilio_to,
        )
        print(message.status)
        print(message.body)

    def get_shortern_url(self, url):
        """gets the short url from bitly"""
        headers = {"Authorization": f"Bearer {bit_token}"}
        params = {"long_url": url}
        response = requests.post(url=bit_url, json=params, headers=headers)
        response.raise_for_status()
        return response.json()["link"]

    def send_emails(self):
        """handles email sending mechanism"""
        users = self.users_data["users"]
        for user in users:
            with smtplib.SMTP(host=yahoo_info["smtp"], port=yahoo_info["port"]) as conn:
                conn.starttls()
                conn.login(user=yahoo_info["email"], password=yahoo_info["password"])
                header = f"To: {user['email']}\nFrom: {yahoo_info['email']}\nSubject: Low price alert!\n\n"
                msg = header
                msg += f"✈ Low price alert!\nOnly ${self.data.price} "
                msg += f"to fly from {self.data.city_from} ({self.data.fly_from}) "
                msg += f"to {self.data.city_to} ({self.data.fly_to}) "
                if self.data.stop_over_cities != 0:
                    msg += f"via {self.data.stop_over_cities[0]} "
                msg += f"from {self.data.out_date} to {self.data.in_date}."
                msg += f"\n\nPlease use this link to get the deal:\n"
                # information in the course does not work any more
                # https://www.google.com/flights?hl=en#flt={flight_info.fly_from}.{flight_info.fly_to}.{flight_info.departure_date}*{flight_info.fly_to}.{flight_info.fly_from}.{flight_info.return_date}
                msg += f"{self.get_shortern_url(self.data.purchase_url)}"
                conn.sendmail(from_addr=yahoo_info["email"], to_addrs=user["email"], msg=msg.encode("utf-8"))


if __name__ == "__main__":
    new_dict = {
        "id": "0488009f4a8700004a06fdac_0|0488009f4a8700004a06fdac_1|009f04884a9d00000b9e0fc3_0|009f04884a9d00000b9e0fc3_1",
        "flyFrom": "BOS",
        "flyTo": "DPS",
        "cityFrom": "Boston",
        "cityCodeFrom": "BOS",
        "cityTo": "Denpasar",
        "cityCodeTo": "DPS",
        "countryFrom": {"code": "US", "name": "United States"},
        "countryTo": {"code": "ID", "name": "Indonesia"},
        "type_flights": ["deprecated"],
        "nightsInDest": 20,
        "quality": 1986.33199,
        "distance": 16246.5,
        "duration": {"departure": 109800, "return": 121200, "total": 231000},
        "price": 1614,
        "conversion": {"USD": 1614, "EUR": 1449},
        "fare": {"adults": 1614, "children": 1614, "infants": 1614},
        "bags_price": {"1": 0},
        "baglimit": {
            "hand_height": 37,
            "hand_length": 50,
            "hand_weight": 7,
            "hand_width": 23,
            "hold_dimensions_sum": 158,
            "hold_height": 52,
            "hold_length": 78,
            "hold_weight": 20,
            "hold_width": 28,
        },
        "availability": {"seats": None},
        "routes": [["BOS", "DPS"], ["DPS", "BOS"]],
        "airlines": ["TK", "QR"],
        "route": [
            {
                "id": "0488009f4a8700004a06fdac_0",
                "combination_id": "0488009f4a8700004a06fdac",
                "flyFrom": "BOS",
                "flyTo": "DOH",
                "cityFrom": "Boston",
                "cityCodeFrom": "BOS",
                "cityTo": "Doha",
                "cityCodeTo": "DOH",
                "airline": "QR",
                "flight_no": 744,
                "operating_carrier": "QR",
                "operating_flight_no": "744",
                "fare_basis": "NLR5R1RI",
                "fare_category": "M",
                "fare_classes": "N",
                "fare_family": "",
                "return": 0,
                "bags_recheck_required": False,
                "vi_connection": False,
                "guarantee": False,
                "last_seen": "2022-03-01T17:09:12.000Z",
                "refresh_timestamp": "2022-03-01T17:09:12.000Z",
                "equipment": None,
                "vehicle_type": "aircraft",
                "local_arrival": "2022-03-29T17:25:00.000Z",
                "utc_arrival": "2022-03-29T14:25:00.000Z",
                "local_departure": "2022-03-28T22:15:00.000Z",
                "utc_departure": "2022-03-29T02:15:00.000Z",
            },
            {
                "id": "0488009f4a8700004a06fdac_1",
                "combination_id": "0488009f4a8700004a06fdac",
                "flyFrom": "DOH",
                "flyTo": "DPS",
                "cityFrom": "Doha",
                "cityCodeFrom": "DOH",
                "cityTo": "Denpasar",
                "cityCodeTo": "DPS",
                "airline": "QR",
                "flight_no": 962,
                "operating_carrier": "QR",
                "operating_flight_no": "962",
                "fare_basis": "NLR5R1RI",
                "fare_category": "M",
                "fare_classes": "N",
                "fare_family": "",
                "return": 0,
                "bags_recheck_required": False,
                "vi_connection": False,
                "guarantee": False,
                "last_seen": "2022-03-01T17:09:12.000Z",
                "refresh_timestamp": "2022-03-01T17:09:12.000Z",
                "equipment": None,
                "vehicle_type": "aircraft",
                "local_arrival": "2022-03-30T16:45:00.000Z",
                "utc_arrival": "2022-03-30T08:45:00.000Z",
                "local_departure": "2022-03-30T02:05:00.000Z",
                "utc_departure": "2022-03-29T23:05:00.000Z",
            },
            {
                "id": "009f04884a9d00000b9e0fc3_0",
                "combination_id": "009f04884a9d00000b9e0fc3",
                "flyFrom": "DPS",
                "flyTo": "IST",
                "cityFrom": "Denpasar",
                "cityCodeFrom": "DPS",
                "cityTo": "Istanbul",
                "cityCodeTo": "IST",
                "airline": "TK",
                "flight_no": 67,
                "operating_carrier": "TK",
                "operating_flight_no": "67",
                "fare_basis": "PF2XPCO",
                "fare_category": "M",
                "fare_classes": "P",
                "fare_family": "",
                "return": 1,
                "bags_recheck_required": False,
                "vi_connection": False,
                "guarantee": False,
                "last_seen": "2022-03-01T04:20:38.000Z",
                "refresh_timestamp": "2022-03-01T04:20:38.000Z",
                "equipment": None,
                "vehicle_type": "aircraft",
                "local_arrival": "2022-04-20T04:45:00.000Z",
                "utc_arrival": "2022-04-20T01:45:00.000Z",
                "local_departure": "2022-04-19T21:00:00.000Z",
                "utc_departure": "2022-04-19T13:00:00.000Z",
            },
            {
                "id": "009f04884a9d00000b9e0fc3_1",
                "combination_id": "009f04884a9d00000b9e0fc3",
                "flyFrom": "IST",
                "flyTo": "BOS",
                "cityFrom": "Istanbul",
                "cityCodeFrom": "IST",
                "cityTo": "Boston",
                "cityCodeTo": "BOS",
                "airline": "TK",
                "flight_no": 81,
                "operating_carrier": "TK",
                "operating_flight_no": "81",
                "fare_basis": "PF2XPCO",
                "fare_category": "M",
                "fare_classes": "P",
                "fare_family": "",
                "return": 1,
                "bags_recheck_required": False,
                "vi_connection": False,
                "guarantee": False,
                "last_seen": "2022-03-01T04:20:38.000Z",
                "refresh_timestamp": "2022-03-01T04:20:38.000Z",
                "equipment": None,
                "vehicle_type": "aircraft",
                "local_arrival": "2022-04-20T18:40:00.000Z",
                "utc_arrival": "2022-04-20T22:40:00.000Z",
                "local_departure": "2022-04-20T15:00:00.000Z",
                "utc_departure": "2022-04-20T12:00:00.000Z",
            },
        ],
        "booking_token": "D1dtTvX-fDlY5Sq4NVzXP9z7re5pbFleBZwLu8EkaS7xM5fBKAd72ATDxjzMy4Iy2CoiHZWq9nyhIlfNFgAaRCpo_pLuJ1n7G2K3BZhX6FlWtVMTf78Vz0m7WB9d7Tf08a8YuuhpFREuVH_hRKeC5ghYvyhHT6r6YFUNTf1etiYVV7UFoYuthS0pui6d6MDhlTUBGP2xlh1mzRYD3LmHeDCyj4v3T2cmZL3RGNH4MuxwLT_BB9YaJABT43caEb1qSD3PEIb1AOq8njYp15pAGqxSgtsZauYhVrXAE6rwC8hanKgdhulb5gSsYqz3ptKLfnwEpUk9dDFS0Oh08JujQZ8dRF_9l9aj4waqvV6VHLeYtIycynQcWqyYXIqCBFJ_gRzXFk9Dv2pmzrkTQYEPBk9hmF0MA1XvpONnXhTVu8WR74tCwm05L7y4wZi9X9YExXRYgLkUOsVLLfvnklbnFOEznEI3hcgkWV5699WzwllTGqXMWA3gjjB3TxU2hXl6X06d8q1c0TdXYy-2JaD99xgwesRT-rWiwtT0eX9dOP9AkQghz_I89VkRxP_v1kEp5",
        "deep_link": "https://www.kiwi.com/deep?from=BOS&to=DPS&flightsId=0488009f4a8700004a06fdac_0%7C0488009f4a8700004a06fdac_1%7C009f04884a9d00000b9e0fc3_0%7C009f04884a9d00000b9e0fc3_1&price=1449&passengers=1&affilid=seanyangflightdealfinder&lang=en&currency=USD&booking_token=D1dtTvX-fDlY5Sq4NVzXP9z7re5pbFleBZwLu8EkaS7xM5fBKAd72ATDxjzMy4Iy2CoiHZWq9nyhIlfNFgAaRCpo_pLuJ1n7G2K3BZhX6FlWtVMTf78Vz0m7WB9d7Tf08a8YuuhpFREuVH_hRKeC5ghYvyhHT6r6YFUNTf1etiYVV7UFoYuthS0pui6d6MDhlTUBGP2xlh1mzRYD3LmHeDCyj4v3T2cmZL3RGNH4MuxwLT_BB9YaJABT43caEb1qSD3PEIb1AOq8njYp15pAGqxSgtsZauYhVrXAE6rwC8hanKgdhulb5gSsYqz3ptKLfnwEpUk9dDFS0Oh08JujQZ8dRF_9l9aj4waqvV6VHLeYtIycynQcWqyYXIqCBFJ_gRzXFk9Dv2pmzrkTQYEPBk9hmF0MA1XvpONnXhTVu8WR74tCwm05L7y4wZi9X9YExXRYgLkUOsVLLfvnklbnFOEznEI3hcgkWV5699WzwllTGqXMWA3gjjB3TxU2hXl6X06d8q1c0TdXYy-2JaD99xgwesRT-rWiwtT0eX9dOP9AkQghz_I89VkRxP_v1kEp5",
        "tracking_pixel": "",
        "facilitated_booking_available": False,
        "pnr_count": 2,
        "has_airport_change": False,
        "technical_stops": 0,
        "throw_away_ticketing": False,
        "hidden_city_ticketing": False,
        "virtual_interlining": True,
        "transfers": [],
        "local_arrival": "2022-03-30T16:45:00.000Z",
        "utc_arrival": "2022-03-30T08:45:00.000Z",
        "local_departure": "2022-03-28T22:15:00.000Z",
        "utc_departure": "2022-03-29T02:15:00.000Z",
    }

    flight_data = FlightData(new_dict)
    link = flight_data.data["deep_link"]
    notif = NotificationManager(flight_data)
    short_link = notif.get_shortern_url(link)
    print(short_link)
