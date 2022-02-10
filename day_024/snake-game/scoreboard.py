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
        # self.high_score = 0
        self.get_highscore()
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        """[summary]"""
        self.goto(0, 260)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        """[summary]"""
        # self.clear()
        self.score += 1
        self.write_score()

    def reset_score(self):
        """[summary]"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.record_highscore()
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     """[summary]"""
    #     self.home()
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    def get_highscore(self):
        """read the highscore record from the data file"""
        with open("data.txt", "r") as f_in:
            recorded_highscore = int(f_in.read())
        self.high_score = recorded_highscore

    def record_highscore(self):
        """store the highscore record to the data file"""
        with open("data.txt", "w") as f_out:
            f_out.write(str(self.high_score))
