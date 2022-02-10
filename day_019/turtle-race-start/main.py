import random
import time
from turtle import Screen, Turtle

STARTING_X = -220
STARTING_Y = -100
SPACE = 50
DESTINATION = 220
MIN_SPEED = 0
MAX_SPEED = 10

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# create all the turtles and put it in the all_turtle list
for ind, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    # new_turtle.speed("fastest")
    space_count = colors.index(color)
    x_pos = STARTING_X
    y_pos = STARTING_Y + space_count * SPACE
    # refactoring: the turtle should print the number for betting
    new_turtle.goto(x=x_pos - 20, y=y_pos)
    new_turtle.write(arg=ind + 1, font=("Courier", 16, "bold"))
    # move the turtle to the start point
    new_turtle.goto(x=x_pos, y=y_pos)
    all_turtles.append(new_turtle)

# refactor: change the input from "color" to "number"
user_bet = screen.numinput(title="Make your bet", prompt="Which turtle will win the race? Enter a number: ")

if user_bet:
    is_race_on = True

while is_race_on:
    # real race logic
    for the_turtle in all_turtles:
        random_distance = random.randint(MIN_SPEED, MAX_SPEED)
        the_turtle.forward(random_distance)
        if the_turtle.xcor() > DESTINATION:
            winning_color = the_turtle.pencolor()
            winning_turtle = all_turtles.index(the_turtle) + 1
            # end the while loop if a turtle wins
            is_race_on = False
            result = Turtle(visible=False)
            result.color(winning_color)
            # result.hideturtle()
            if int(user_bet) == winning_turtle:
                # instead of printing in command prompt, print that on the screen
                # print(f"You've won! The {winning_color} turtle is the winner!")
                result.write(
                    f"You've won!\nThe '{winning_color.upper()}' turtle is the winner!",
                    align="center",
                    font=("Arial", 12, "bold"),
                )
            else:
                # instead of printing in command prompt, print that on the screen
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                result.write(
                    f"You've lost!\nThe '{winning_color.upper()}' turtle is the winner!",
                    align="center",
                    font=("Arial", 12, "bold"),
                )
            # prevent another turtle gets to this the final point
            break

# refactor: shut off the program after 3 seconds
time.sleep(3)
screen.bye()

# TODO: save the result as an image
