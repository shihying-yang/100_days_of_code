import random

import pandas

# number = [1, 2, 3]
# # add 1 to the list
# new_number = [num + 1 for num in number]
# print(new_number)

# name = "Angela"
# letter_list = [letter for letter in name]
# print(letter_list)

# # create a list from range and double it
# # range(1,5) --> [2, 4, 6, 8]
# double_list = [num * 2 for num in range(1, 5)]
# print(double_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

# # take the names with 5 letters or more and make them uppercase
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# defination: new_dict = [key:value for (key, value) in dict.items() if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_score = {name: random.randint(1, 100) for name in names}
# print(student_score)

# passed_students = {name: score for (name, score) in student_score.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# for (key, value) in student_dict.items():
#     print(key, value)
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

## Loop thru a data frame
# for (key, value) in student_data_frame.items():
#     print(key, value)
for (index, row) in student_data_frame.iterrows():
    # print(index, row)
    # print(f"{row.student}: {row.score}")
    if row.student == "Angela":
        print(row.score)
