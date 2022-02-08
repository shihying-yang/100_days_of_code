"""Scoreboard class"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self):
        """[summary]"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        """[summary]"""
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        """[summary]"""
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=FONT)
