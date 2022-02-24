import datetime as dt
import requests
import sys

sys.path.insert(0, "../..")

from personal_config import my_info

GENDER = "male"
WEIGHT_KG = 88.5
HEIGHT_CM = 184
AGE = 46

nutritionix_app_id = my_info["nutritionix_app_id"]
nutritionix_app_key = my_info["nutritionix_app_key"]

nutritionix_url = "https://trackapi.nutritionix.com"

sheety_workout_id = my_info["sheety_workout_id"]
sheety_url = "https://api.sheety.co"
sheety_workout_sheet_token = my_info["sheety_workout_sheet_token"]


def get_data_from_nutritionix(exercise):
    """Get the exercise data from nutritionix API.

    :param exercise: exercise input
    :type exercise: str
    :return: exercise data
    :rtype: dict
    """
    nutritionix_exercise_url = f"{nutritionix_url}/v2/natural/exercise"
    nutritionix_headers = {
        "x-app-id": nutritionix_app_id,
        "x-app-key": nutritionix_app_key,
        "Content-Type": "application/json",
    }
    nutritionix_params = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }
    response = requests.post(
        url=nutritionix_exercise_url, headers=nutritionix_headers, json=nutritionix_params
    )
    return response.json()


def update_google_sheet(exercise_dict):
    """Update the google sheet with the exercise data.

    :param exercise_dict: exercise data
    :type exercise_dict: dict
    """
    now = dt.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    headers = {
        "Authorization": sheety_workout_sheet_token,
    }
    for workout in exercise_dict["exercises"]:
        body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": workout["user_input"].title(),
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],
            }
        }
        response = requests.post(
            url=f"{sheety_url}/{sheety_workout_id}/workoutTracking2/workouts", json=body, headers=headers
        )
        # print(response.status_code)


if __name__ == "__main__":
    exercise_input = input("Tell me which exercises you did: ")
    exercise_data = get_data_from_nutritionix(exercise_input)
    update_google_sheet(exercise_data)

# ------- test data as below -------
"""
exercise_data = {
    "exercises": [
        {
            "tag_id": 317,
            "user_input": "ran",
            "duration_min": 20.01,
            "met": 9.8,
            "nf_calories": 289.24,
            "photo": {
                "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
                "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
                "is_user_uploaded": False,
            },
            "compendium_code": 12050,
            "name": "running",
            "description": None,
            "benefits": None,
        },
        {
            "tag_id": 100,
            "user_input": "walked",
            "duration_min": 37.28,
            "met": 3.5,
            "nf_calories": 192.46,
            "photo": {
                "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg",
                "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg",
                "is_user_uploaded": False,
            },
            "compendium_code": 17190,
            "name": "walking",
            "description": None,
            "benefits": None,
        },
    ]
}
"""
