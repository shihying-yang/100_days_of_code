import random
from turtle import Turtle, Screen

STARTING_X = -230
STARTING_Y = -100
SPACE = 50
DESTINATION = 220
MIN_SPEED = 0
MAX_SPEED = 10

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
).lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# create all the turtles and put it in the all_turtle list
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    space_count = colors.index(color)
    x_pos = STARTING_X
    y_pos = STARTING_Y + space_count * SPACE
    new_turtle.goto(x=x_pos, y=y_pos)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    # lazy gaming
    if user_bet.startswith("r"):
        user_bet = "red"
    elif user_bet.startswith("o"):
        user_bet = "orange"
    elif user_bet.startswith("y"):
        user_bet = "yellow"
    elif user_bet.startswith("g"):
        user_bet = "green"
    elif user_bet.startswith("b"):
        user_bet = "blue"
    elif user_bet.startswith("p"):
        user_bet = "purple"
    else:
        user_bet = "black"

while is_race_on:
    # real race logic
    for the_turtle in all_turtles:
        random_distance = random.randint(MIN_SPEED, MAX_SPEED)
        the_turtle.forward(random_distance)
        if the_turtle.xcor() > DESTINATION:
            winning_color = the_turtle.pencolor()
            # end the while loop here
            is_race_on = False
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            # prevent another turtle gets to this the final point
            break

screen.exitonclick()
