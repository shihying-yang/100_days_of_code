"""Scoreboard class"""

import time
from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self):
        """init object"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        """write score"""
        # self.color("white")
        self.goto(-300, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(300, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))

    def increase_score(self, left_or_right):
        """increase score"""
        if left_or_right == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.write_score()
