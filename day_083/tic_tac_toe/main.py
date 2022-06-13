"""Build a text-based version of the Tic Tac Toe game.
"""
from cgi import print_environ
from random import randint
import time


class Player:
    """Player class"""

    def __init__(self, name, symbol):
        """initialize player"""
        self.name = name
        self.symbol = symbol
        # self.occupied = []


def re_init_game():
    """re-initialize the game"""
    marks = [x for x in range(10)]
    marks[0] = "X"
    turns = 0
    print(f"marks: {marks}")
    return marks, turns


def check_win(board_loc):
    """Check if there is a winner."""
    return (
        board_loc[1] == board_loc[2] == board_loc[3]
        or board_loc[4] == board_loc[5] == board_loc[6]
        or board_loc[7] == board_loc[8] == board_loc[9]
        or board_loc[1] == board_loc[4] == board_loc[7]
        or board_loc[2] == board_loc[5] == board_loc[8]
        or board_loc[3] == board_loc[6] == board_loc[9]
        or board_loc[1] == board_loc[5] == board_loc[9]
        or board_loc[3] == board_loc[5] == board_loc[7]
    )


def print_board(marks):
    """print the current board"""
    board = f"\nThe board:\n\n     |     |     \n  {marks[1]}  |  {marks[2]}  |  {marks[3]}  \n-----|-----|-----\n  {marks[4]}  |  {marks[5]}  |  {marks[6]}  \n-----|-----|-----\n  {marks[7]}  |  {marks[8]}  |  {marks[9]}  \n     |     |     \n"
    print(board)


if __name__ == "__main__":
    marks, turns = re_init_game()

    name1 = input("Player 1, what is your name?\n>> ")
    p1 = Player(name1, "X")
    print(f"{p1.name}, welcome to the tic-tac-toe game, your symbol is 'O'\n")
    name2 = input("Player 2, what is your name?\n>> ")
    p2 = Player(name2, "O")
    print(f"{p2.name}, welcome to the tic-tac-toe game, your symbol is 'X'")

    # TODO: add a loop to play the game again if the user wants to
    game_on = True
    while game_on:
        print_board(marks)
        if turns % 2 == 0:
            player = p1
        else:
            player = p2

        if turns == 9:
            print("It's a tie!")
            game_on = False
            continue

        if not check_win(marks):
            print(f"{player.name}, it is your turn.")
            correct_input = False
            loc = 0
            while not correct_input:
                try:
                    loc = int(input("Where would you like to place your mark (1-9)? "))
                    correct_input = True
                except ValueError:
                    print("Please enter a number between 1 and 9.")
                if marks[loc] == "X" or marks[loc] == "O":
                    print("The space is occupied. Please choose another location.")
                    correct_input = False

            marks[loc] = player.symbol
        else:
            if player == p1:
                print(f"{p2.name}, you won!")
            else:
                print(f"{p1.name}, you won!")
            game_on = False
        turns += 1
