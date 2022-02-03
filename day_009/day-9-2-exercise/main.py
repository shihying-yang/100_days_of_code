travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(to_add_country, times_visited, cities_visited):
    """
    Add a new country to the travel_log dictionary
    """
    travel_log.append({"country": to_add_country, "visits": times_visited, "cities": cities_visited})


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
