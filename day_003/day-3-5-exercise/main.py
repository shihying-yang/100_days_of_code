# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
true_score = 0
love_score = 0

for ch in ["t", "r", "u", "e"]:
    true_score += name1.lower().count(ch)
    true_score += name2.lower().count(ch)

for ch in ["l", "o", "v", "e"]:
    love_score += name1.lower().count(ch)
    love_score += name2.lower().count(ch)

true_love_score = int(str(true_score) + str(love_score))

if true_love_score < 10 or true_love_score > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score >= 40 and true_love_score <= 50:
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}.")
