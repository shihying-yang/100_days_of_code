"""This is used for user registration"""
import sys

import requests

sys.path.insert(0, "../../")

from personal_config import my_info

sheety_flight_id = my_info["sheety_flight_id"]
sheety_flight_sheet_token = my_info["sheety_flight_sheet_token"]
sheety_url = "https://api.sheety.co"


def get_users():
    """test function to see if I can get information from the users sheet"""
    headers = {"Authorization": sheety_flight_sheet_token}
    response = requests.get(f"{sheety_url}/{sheety_flight_id}/flightDeals2/users", headers=headers)
    response.raise_for_status()
    return response.json()


def update_users(f_name, l_name, em):
    """function to update the users google sheet with first name, last name, and email"""
    headers = {"Authorization": sheety_flight_sheet_token}
    params = {
        "user": {
            "firstName": f_name,
            "lastName": l_name,
            "email": em,
        }
    }
    response = requests.post(
        url=f"{sheety_url}/{sheety_flight_id}/flightDeals2/users", json=params, headers=headers
    )
    response.raise_for_status()
    # print(response.status_code)
    # print(response.json())
    return response.status_code


if __name__ == "__main__":
    print("Welcome to Sean's Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    email_again = input("Type your email again.\n")
    if email == email_again:
        ret = update_users(first_name, last_name, email)
        if ret == 200:
            print("You're in the club!")
        else:
            print("Something went wrong. Please try again later.")
    else:
        print("Email does not match.")
