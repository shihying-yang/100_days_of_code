"""A text version of Higher Lower Game
"""
import random
from os import system

from art import logo, vs
from game_data import data


def compare_followers(list_1, list_2):
    """compare the follower count of two lists

    :param list_1: first list
    :type list_1: list
    :param list_2: second list
    :type list_2: list
    :return: list with higher follower count
    :rtype: list
    """
    first_follower_count = list_1.get("follower_count")
    second_follower_count = list_2.get("follower_count")
    if first_follower_count > second_follower_count:
        return list_1
    else:
        return list_2


def start_game():
    """The process to start the game. This will only happen once.

    :return: item randomly selected from the data list
    :rtype: list
    """
    system("clear")
    print(logo)
    # randomly pick the first item
    item_1 = random.choice(data)
    data.remove(item_1)
    return item_1


if __name__ == "__main__":
    correct_guess = True
    score = 0
    while correct_guess:
        # when the score is 0, this is the first time the game is played
        if score == 0:
            compare_a = start_game()  # do this once
        else:
            print(f"You're right! Current score: {score}")
        
        # start game logic
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']} from {compare_a['country']}.")
        print(vs)
        # compare_b is always randomly picked during the game process
        compare_b = random.choice(data)
        data.remove(compare_b)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']} from {compare_b['country']}.")
        # ask the user to make a guess to see if a is higher or b is higher
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        guessed_list = []
        # set the guessed list to the item that the user guessed
        if guess == "a":
            guessed_list = compare_a
        elif guess == "b":
            guessed_list = compare_b
        else:
            pass
        # get the higher list of the two
        higher = compare_followers(compare_a, compare_b)

        # clear the screen ang print the logo, wait for next result
        system("clear")
        print(logo)

        # if guessed correctly, add 1 to the score, else end the game
        if guessed_list == higher:
            score += 1
            compare_a = compare_b
            if len(data) == 0:
                correct_guess = False
                print(f"You finish the game! Final score is {score}.")
        else:
            correct_guess = False
            print(f"Sorry, that's wrong. Final score: {score}")
