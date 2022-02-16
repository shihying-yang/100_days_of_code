# # FileNotFoundError
# with open("a_file.txt", "r") as f_in:
#     f_in.read()

# # KeyError
# a_dictionary = {"key": "value"}
# Value = a_dictionary["nonexistent_key"]

# # IndexError
# fruit = ["Apple", "Banana", "Pear"]
# fruit[3]

# # TypeError
# text = "abc"
# print(text + 5)


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something.")
# except KeyError as error_message:
#     print(f"That's key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     # raise KeyError
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
