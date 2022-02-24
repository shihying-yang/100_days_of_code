import datetime as dt
import requests
import sys

sys.path.insert(0, "../..")

from personal_config import my_info

USERNAME = my_info["pixela_username"]
TOKEN = my_info["pixela_token"]
GRAPH_ID = my_info["pixela_code_graph_id"]

pixela_end_point = "https://pixe.la"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
create_user_endpoint = f"{pixela_end_point}/v1/users"
# # create user
# response = requests.post(url=create_user_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Graph",
    "unit": "Mins",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
create_graph_endpoint = f"{pixela_end_point}/v1/users/{USERNAME}/graphs"
# # create a new graph
# response = requests.post(
#     url=create_graph_endpoint, json=graph_config, headers=headers
# )
# print(response.text)

today = dt.datetime.now()
today_str = today.strftime("%Y%m%d")
yesterday = dt.datetime.now() - dt.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y%m%d")

pixel_data = {
    "date": yesterday_str,
    "quantity": "180",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
create_pixel_endpoint = f"{pixela_end_point}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# # create a pixel
# response = requests.post(url=create_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# update a pixel
pixel_update = {
    "quantity": "110",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

update_pixel_endpoint = f"{pixela_end_point}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_str}"
response = requests.put(url=update_pixel_endpoint, json=pixel_update, headers=headers)
print(response.text)
