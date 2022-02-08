"""Food class file"""

from turtle import Turtle
import random

BOUNDARY = 260


class Food(Turtle):
    """Food class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """food goes to a random location"""
        random_x = random.randint(-1 * BOUNDARY, BOUNDARY)
        random_y = random.randint(-1 * BOUNDARY, BOUNDARY)
        self.goto(random_x, random_y)
