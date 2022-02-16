"""car manager file, including CarManager class and Car class"""
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 280


class CarManager:
    """CarManager class"""

    def __init__(self):
        """initilize the CarManager class"""
        self.cars = []
        self.add_car()

    def add_car(self):
        """add a car instance to the manager"""
        # randomize the creation of the car
        add = random.choice(range(1, 11))
        # if add == 1:
        if add % 3 == 0:
            self.cars.append(Car())

    def move_cars(self):
        """make sure the car is continuously moving"""
        for car in self.cars:
            car.move()

    def clean_up(self):
        """create a method to handle the memory usage"""
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)


class Car(Turtle):
    """Car class"""

    def __init__(self):
        """init a car instance"""
        super().__init__(shape="square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        # set the car to come out from a random y position
        random_y = random.randint(-250, 250)
        self.goto(STARTING_X, random_y)

    def move(self):
        """handles the car movement"""
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
