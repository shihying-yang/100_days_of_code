"""create a squirrel_count.csv with 2 columns, Fur Color and Count"""
import pandas

sq_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(sq_data.head())

# gray_sq_data = sq_data[sq_data["Primary Fur Color"] == "Gray"]
# print(type(gray_sq_data))

# print(len(sq_data["Primary Fur Color"]))
# print(sq_data["Primary Fur Color"].value_counts())

# output_data = sq_data["Primary Fur Color"].value_counts()
# pandas.DataFrame(output_data).to_csv('squirrel_count.csv')

# new_data = pandas.read_csv("squirrel_count.csv")
# print(new_data.to_dict())


# Angela's method
gray_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_sq_count, red_sq_count, black_sq_count],
}

pan_data = pandas.DataFrame(data_dict)
pandas.DataFrame(data_dict).to_csv('squirrel_count.csv')
