"""scoreboard file"""
from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self):
        """init scoreboard"""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.score = 0

    def update_score(self):
        """udpate the score"""
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def add_score(self):
        """add a point to the score (when the player wins)"""
        self.score += 1
        self.update_score()

    def game_over(self):
        """if the player is hit by the car, print Game Over"""
        self.home()
        self.color("red")
        self.write("Game Over", align="center", font=("Arial", 30, "bold"))
