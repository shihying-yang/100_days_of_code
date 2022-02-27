"""DataManager class to handle the Google Sheet interactions (Sheety API)"""
import sys
from pprint import pprint

import requests

sys.path.insert(0, "../..")

from personal_config import my_info

sheety_id = my_info["sheety_flight_id"]
sheety_auth = my_info["sheety_flight_sheet_token"]


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        """Init the class with the basic params for each function"""
        self.sheety_project = "flightDeals2"
        self.sheety_sheet = "prices"
        self.sheety_url = f"https://api.sheety.co"
        # gather that data when initialized
        self.data = self.get_data()

    def get_data(self):
        """Get the full data from the passed in google sheet (check init)"""
        response = requests.get(
            url=f"{self.sheety_url}/{sheety_id}/{self.sheety_project}/{self.sheety_sheet}",
            headers={"Authorization": sheety_auth},
        )
        response.raise_for_status()
        return response.json()

    def put_city_code(self, city_code, row_id):
        """Put in the missing iataCode (city code) gathered from kiwi api"""
        for da in self.data["prices"]:
            if da["id"] == row_id:
                current_data = da
                break
        # return current_data
        current_data["iataCode"] = city_code
        message = {"price": current_data}
        response = requests.put(
            url=f"{self.sheety_url}/{sheety_id}/{self.sheety_project}/{self.sheety_sheet}/{row_id}",
            headers={"Authorization": sheety_auth},
            json=message,
        )
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    data_manager = DataManager()
    sheet_data = data_manager.data
    pprint(sheet_data)
    # test put data
    print(data_manager.put_city_code("HKG", 4))
