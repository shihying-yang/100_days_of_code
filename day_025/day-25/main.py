"""day 25 - main.py"""


# with open("weather_data.csv", "r") as f_in:
#     weather_data = f_in.readlines()
# print(weather_data)

# import csv

# with open("weather_data.csv", "r") as f_in:
#     data = csv.reader(f_in)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

from audioop import avg

import pandas

data = pandas.read_csv("weather_data.csv")

# # basic pandas structure
# print(data)
# print(data.temp)
# print(data['temp'])

# print(type(data))
# print(type(data.temp))

# # convert a DataFrame to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # convert a Series to a list
# temp_list = data["temp"].to_list()
# print(temp_list)

# # find the average temperature from the data
# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(avg_temp)

# # the easier way
# print(data["temp"].mean())


# # find the highest temperatures
# print(data["temp"].max())

# # Get Data in column
# print(data["condition"])
# print(data.condition)

# # Get Data in row
# print(data[data.day == "Monday"])

# # Get the data where the temperature is the highest
# highest_temp_row = data[data.temp == data.temp.max()]
# print(highest_temp_row)

# monday = data[data.day == "Monday"]
# # print(type(monday))
# # print(monday.condition)
# monday_temp_f = int(monday.temp) * 9 / 5 + 32
# print(monday_temp_f)

# # Create a dataframe from scratch

# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")
