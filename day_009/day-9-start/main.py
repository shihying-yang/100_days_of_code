# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])

# # Loop thru a dictionary
# for key in programming_dictionary:
#     # print(key)
#     print(f"{key}:  {programming_dictionary[key]}")


###############################################################################
# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nesting a list inside a dictionary
travel_log = {
    "France": ["Paris", "Lyon", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary inside a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lyon", "Dijon"],
        "total_visits": 12,
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Italy": {
        "cities_visited": ["Rome", "Milan", "Venice"],
        "total_visits": 5,
    },
}

# print(travel_log["Italy"]["cities_visited"][0])

# Nesting a Dictionary in a list
travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lyon", "Dijon"], "total_visits": 12},
    {"country": "Germamy", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
]

print(travel_log[0]["cities_visited"][1])
