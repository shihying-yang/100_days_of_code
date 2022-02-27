"""Main function for the flight search which incorporates Google Sheet 
(sheety api). and kiwi api"""
# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import datetime as dt
from pprint import pprint

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

today = dt.date.today().strftime("%Y-%m-%d")

if __name__ == "__main__":
    # Check Google Sheet first to get the data (for checking)
    data_manager = DataManager()
    wish_data = data_manager.data
    """
    wish_data = {
        "prices": [
            # {"city": "Paris", "iataCode": "", "lowestPrice": 1600, "id": 2},
            # {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 600, "id": 3},
            # {"city": "Hong Kong", "iataCode": "", "lowestPrice": 1600, "id": 4},
            {"city": "Cancun", "iataCode": "CUN", "lowestPrice": 220, "id": 5},
            # {"city": "Lisbon", "iataCode": "LIS", "lowestPrice": 500, "id": 6},
            # {"city": "Bali", "iataCode": "DPS", "lowestPrice": 1300, "id": 7},
            # {"city": "Taipei", "iataCode": "TPE", "lowestPrice": 1000, "id": 8},
        ]
    }
    """

    # original idea (scratched): pass in the full dictionary to flight search (for checking)
    # modified: only pass in each city data to flight search
    for ind, data in enumerate(wish_data["prices"]):
        flight_search = FlightSearch(data)
        # handle missing iataCode before next step
        if data["iataCode"] == "":
            city_code = flight_search.get_city_code()
        flight_search_result = flight_search.get_flight_data()

        # grab all the data from the flight search result
        datas = flight_search_result["data"]
        if len(datas) > 0:
            print(f"{len(datas)} flights found for {data['city']}")
            # if I can find anything, just sending 1 SMS is good enough
            for ind_temp, data_temp in enumerate(datas):
                flight_data = FlightData(data_temp)
                if ind_temp == 0:
                    new_notif = NotificationManager(flight_data)
                    new_notif.send_sms()
                with open(f"flight_search_{data['city']}_{today}.txt", "a", encoding="utf-8") as f_in:
                    f_in.write(f"{data_temp}\n")
        else:
            # no result found, print out the message
            print(f"No result found for {data['city']}")
