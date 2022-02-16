# Data Types

# print(len(12352)) # --> TypeError: object of type 'int' has no len()

## String

print("Hello"[0])  # index always starts from 0

print("Hello"[-1])

print("123" + "456")

print("hello" + " world")

## Integer

print(123 + 456)

print(123_456_789)

## Float

print(3.14159)

## Boolean
print(True)
print(False)

## Type Error

num_char = len(input("What is your name? "))
# # print("Your name has " + str(num_char) + " characters.")
# # print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# a = str(123)
a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

## Mathematical Operations
print(3 + 5)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(2 ** 3)

# PEMDAS
# () > ** > * = / > + = -

print(3 * 3 + 3 / 3 - 3)  # 7.0
print(3 * (3 + 3) / 3 - 3)  # 3.0

## Number Manipulation

print(int(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)
print(type(8 // 3))

result = 4 / 2
result /= 2
print(result)

score = 0
# user scores a point
score += 1

print(score)

## F-strings
score = 0
height = 1.8
isWinning = True

# print("Your score is " + str(score) + str(height) + str(isWinning))
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")
