"""player class file"""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Turtle class"""

    def __init__(self):
        """init player (turtle)"""
        super().__init__(shape="turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """handles the players movement. Going north only in this case."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def check_win(self):
        """check if the player goes beyond the destination, return True
        if it does; otherwise return False"""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def next_stage(self):
        """Set the player to go back to the starting point"""
        self.goto(STARTING_POSITION)

    def colide_with_car(self, car):
        """Check if the player is hit by a car. Return True if it is;
        otherwise return False"""
        if self.distance(car) < 20:
            return True
        return False
