import datetime as dt
import sys

import requests

sys.path.insert(0, "../../")

from personal_config import my_info

my_loc = my_info["my_location"]


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# # print(response.status_code)
# # if response.status_code != 200:
# #     raise Exception("ERROR: API request unsuccessful.")

# response.raise_for_status()

# data = response.json()["iss_position"]
# # print(data)
# longitude = data["longitude"]
# latitude = data["latitude"]

# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {"lat": my_loc["lat"], "lng": my_loc["lng"], "formatted": 0}

# response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# # print(data)
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]

# sunrise_hour = sunrise.split("T")[1].split(":")[0]
# sunset_hour = sunset.split("T")[1].split(":")[0]
# print(sunrise, sunset)

now = dt.datetime.now(dt.timezone.utc)
now_hour = now.hour
print(now_hour)
