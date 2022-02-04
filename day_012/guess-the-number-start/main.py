# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from os import system

LOGO = """ __    _  __   __  __   __  _______  _______  ______      _______  __   __  _______  _______  _______  ___   __    _  _______ 
|  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |       ||  | |  ||       ||       ||       ||   | |  |  | ||       |
|   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |    ___||  | |  ||    ___||  _____||  _____||   | |   |_| ||    ___|
|       ||  |_|  ||       ||       ||   |___ |   |_||_   |   | __ |  |_|  ||   |___ | |_____ | |_____ |   | |       ||   | __ 
|  _    ||       ||       ||  _   | |    ___||    __  |  |   ||  ||       ||    ___||_____  ||_____  ||   | |  _    ||   ||  |
| | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  |   |_| ||       ||   |___  _____| | _____| ||   | | | |   ||   |_| |
|_|  |__||_______||_|   |_||_______||_______||___|  |_|  |_______||_______||_______||_______||_______||___| |_|  |__||_______|
"""
# Put the number of turms in constant var, to make it easy if we need to change game later.
EASY_TURNS = 10
HARD_TURNS = 5


def start_game():
    """Start game and select level

    :return: choice of level
    :rtype: boolean
    """
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().startswith("h")
    if level_hard:
        return True
    return False


def guessing(correct_number, times):
    """Guess the number

    :param correct_number: correct number
    :type correct_number: int
    :param times: number of turns
    :type times: int
    :return: None
    :rtype: None
    """
    while times > 0:
        print(f"You have {times} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == correct_number:
            print("You got it! 👍")
            break
        elif guess > correct_number:
            print("Too high! Go lower! ⬇")
        else:
            print("Too low! Go higher! ⬆")
        times -= 1
        if times == 0:
            print("You ran out of guesses! you lose.")
    print(f"The correct answer is {correct_number}.")


if __name__ == "__main__":
    # make the game continuous (extra from request)
    continue_playing = True
    while continue_playing:
        answer = random.randint(1, 100)
        # print(f"debugging purpose, the answer is {answer}")
        level_is_hard = start_game()
        times_left = EASY_TURNS
        if level_is_hard:
            times_left = HARD_TURNS

        guessing(answer, times_left)
        continue_playing = input("Do you want to play again? (y/n): ").lower().startswith("y")
        if continue_playing:
            system("clear")
    print("Thanks for playing!")
