"""ball class"""

from turtle import Turtle
from random import choice

MOVING_DISTANCE = 15


class Ball(Turtle):
    """Ball class"""

    def __init__(self) -> None:
        """init ball object"""
        super().__init__(shape="circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        # start with random direction
        self.up_down = choice([1, -1])
        self.left_right = choice([1, -1])
        # self.up_down = 1
        # self.left_right = 1
        self.move()

    def move(self):
        """keep moving the ball forward"""
        new_coordinates = (
            self.xcor() + self.left_right * MOVING_DISTANCE,
            self.ycor() + self.up_down * MOVING_DISTANCE,
        )
        self.goto(new_coordinates)
        # print(new_coordinates)

    def bounce_up_down(self):
        """bounce when hit the wall on top or bottom"""
        self.up_down *= -1
        # print("up_down")

    def bounce_left_right(self):
        """bounce when hit the paddle"""
        self.left_right *= -1
        # print("left_right")

    def reset_position(self):
        """reset the ball back to where it was"""
        self.home()
        self.up_down = choice([-1, 1])
        self.left_right = choice([-1, 1])
