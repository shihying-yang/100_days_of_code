import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

# it's a good idea to store the ascii art in a list.
game_images = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if your_choice < 3:
    print(game_images[your_choice])

pc_choice = random.randint(0, 2)
print(f"Computer chose:")
print(game_images[pc_choice])

if your_choice == pc_choice:
    print("It's a tie!")
elif (
    (your_choice == 0 and pc_choice == 1)
    or (your_choice == 1 and pc_choice == 2)
    or (your_choice == 2 and pc_choice == 0)
):
    print("You lose!")
elif (
    (your_choice == 0 and pc_choice == 2)
    or (your_choice == 1 and pc_choice == 0)
    or (your_choice == 2 and pc_choice == 1)
):
    print("You win!")
else:
    print("You input an invalid number, you lose!")
