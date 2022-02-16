# for loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# range function
for number in range(1, 10):  # 10 is not printed
    print(number)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
