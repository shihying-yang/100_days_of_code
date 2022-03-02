"""FlightSearch class to handle all the actions with kiwi Flight search API"""
import datetime as dt
import sys

import requests

sys.path.insert(0, "../..")

from personal_config import my_info

from flight_data import FlightData

kiwi_api_key = my_info["kiwi_api_key"]
start_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
end_date = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")
fly_from = my_info["fly_from"]


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, wish_data):
        """init the class with usual data"""
        self.start_date = start_date
        self.end_date = end_date
        self.wish_data = wish_data
        self.url = f"https://tequila-api.kiwi.com"
        self.headers = {"apikey": kiwi_api_key}

    def get_city_code(self):
        """get the city code from the city name"""
        if self.wish_data["iataCode"] != "":
            return self.wish_data["iataCode"]
        else:
            # sample url
            # https://tequila-api.kiwi.com/locations/query?term=Hong%20Kong&locale=en-US&location_types=airport
            message = {
                "term": self.wish_data["city"],
                "locale": "en-US",
                "location_types": "airport",
            }
            response = requests.get(url=f"{self.url}/locations/query", headers=self.headers, params=message)
            if response.status_code == 200:
                city_code = response.json()["locations"][0]["city"]["code"]
                self.wish_data["iataCode"] = city_code
                return city_code
            else:
                return "Not Found"

    def get_flight_data(self, stop_over=0):
        """check the api for flghts"""
        # test url
        # https://tequila-api.kiwi.com/v2/search?fly_from=BOS&fly_to=PAR&date_from=28%2F02%2F2022&date_to=28%2F04%2F2022&curr=USD&price_to=1800&max_stopovers=0&vehicle_type=aircraft&limit=500
        message = {
            "fly_from": fly_from,
            "fly_to": self.wish_data["iataCode"],
            "date_from": self.start_date,
            "date_to": self.end_date,
            # "flight_type": "round",  # deprecated
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD",
            "max_stopovers": stop_over,
            "price_to": self.wish_data["lowestPrice"],
        }
        response = requests.get(url=f"{self.url}/v2/search", headers=self.headers, params=message)
        return response.json()


if __name__ == "__main__":
    # wish_data = {"city": "Hong Kong", "iataCode": "", "lowestPrice": 900, "id": 4}
    wish_data = {"city": "Bali", "iataCode": "DPS", "lowestPrice": 1800, "id": 2}
    flight_search = FlightSearch(wish_data)
    flight_search.get_city_code()
    response = flight_search.get_flight_data()
    datas = response["data"]
    if len(datas) > 0:
        for data in datas[:2]:
            flight_data = FlightData(data)
            print(flight_data)
    else:
        response = flight_search.get_flight_data(stop_over=2)
        datas = response["data"]
        if len(datas) > 0:
            for data in datas[:2]:
                flight_data = FlightData(data, stop_over=2)
                print(flight_data)
