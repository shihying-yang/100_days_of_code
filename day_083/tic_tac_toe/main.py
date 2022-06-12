"""Build a text-based version of the Tic Tac Toe game.
"""
from random import randint
import time

"""
Thinking process:

ask name for player 1 and assign "X" as the symbol
ask name for player 2 and assign "O" as the symbol

while game is not over:
    print the board
    ...

"""


# initialize the board
marks = [x for x in range(10)]
board = f"\nThe board:\n\n     |     |     \n  {marks[1]}  |  {marks[2]}  |  {marks[3]}  \n-----|-----|-----\n  {marks[4]}  |  {marks[5]}  |  {marks[6]}  \n-----|-----|-----\n  {marks[7]}  |  {marks[8]}  |  {marks[9]}  \n     |     |     \n"
TURNS = 0


class Player:
    """Player class"""

    def __init__(self, name, symbol):
        """initialize player"""
        self.name = name
        self.symbol = symbol
        # self.occupied = []

    # def show_occupied(self):
    #     """Show occupied spaces"""
    #     # print(f"{self.name}'s occupied spaces: {self.occupied}")
    #     return self.occupied


def re_init_game():
    global marks
    global TURNS
    marks = [x for x in range(10)]
    TURNS = 0


def check_win():
    """Check if there is a winner."""
    return (
        marks[1] == marks[2] == marks[3]
        or marks[4] == marks[5] == marks[6]
        or marks[7] == marks[8] == marks[9]
        or marks[1] == marks[4] == marks[7]
        or marks[2] == marks[5] == marks[8]
        or marks[3] == marks[6] == marks[9]
        or marks[1] == marks[5] == marks[9]
        or marks[3] == marks[5] == marks[7]
    )


def upfdate_baord(loc):
    """Update the board with the player's move."""
    pass


def print_board():
    """print the current board"""
    print(board)


if __name__ == "__main__":
    re_init_game()

    name1 = input("Player 1, what is your name?\n>> ")
    p1 = Player(name1, "X")
    print(f"{p1.name}, welcome to the tic-tac-toe game, your symbol is X\n")
    name2 = input("Player 2, what is your name?\n>> ")
    p2 = Player(name2, "O")
    print(f"{p2.name}, welcome to the tic-tac-toe game, your symbol is O")

    game_on = True
    while game_on:
        # print_board()
        if TURNS % 2 == 0:
            player = p1
        else:
            player = p2

        if not check_win():
            print_board()
            print(f"{p1.name}, it's your turn")

            occupied = False
            while not occupied:
                try:
                    loc = int(input(f"{player.name}, where would you like to move?\n>> "))
                except:
                    print(f"You must put in a location between 1 and 9.")
                    continue
                if marks[loc] == "O" or marks[loc] == "X":
                    print("That space is already occupied, please try a different location.")
                else:
                    marks[loc] = player.symbol
                    # player.occupied.append(loc)
                TURNS += 1
                occupied = True
        else:
            print(f"{player.name} wins! The game is over.")
            game_on = False
