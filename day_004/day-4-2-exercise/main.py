import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# upper_limit = len(names)
# lucky_number = random.randint(0, upper_limit - 1)
# lucky_name = names[lucky_number]

lucky_name = random.choice(names)
print(f"{lucky_name} is going to buy the meal today!")
