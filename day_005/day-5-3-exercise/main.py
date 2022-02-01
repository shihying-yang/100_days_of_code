# Write your code below this row 👇

# Write a program that calculates the sum of all the even numbers
# from 1 to 100. Thus, the first even number would be 2 and the last one
# is 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
