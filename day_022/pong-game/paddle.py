"""Paddle Class"""

from turtle import Turtle

STARTING_X = 350
STARTING_Y = 0
MOVING_DISTANCE = 20
PADDLE_LENGTH = 5


class Paddle(Turtle):
    """Paddle Class"""

    def __init__(self, left_or_right, height_limit):
        super().__init__(shape="square")
        # self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if left_or_right == "left":
            x = -1 * STARTING_X
        else:
            x = STARTING_X
        self.goto(x, STARTING_Y)
        self.height_limit = height_limit

    def go_up(self):
        """move the paddle up"""
        if self.ycor() < (self.height_limit / 2) - 20 - (PADDLE_LENGTH * 20 / 2):
            self.goto(self.xcor(), self.ycor() + MOVING_DISTANCE)

    def go_down(self):
        """move the paddle down"""
        if self.ycor() > (-1 * self.height_limit / 2) + 20 + (PADDLE_LENGTH * 20 / 2):
            self.goto(self.xcor(), self.ycor() - MOVING_DISTANCE)
