"""Guess US State game"""

import turtle
import pandas
import time

TOTAL_STATES = 50
SCORE_FONT = ("Arial", 10, "normal")
ANNOUNCE_FONT = ("Arial", 30, "normal")

# setup screen and load the US map
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# get the state data from the csv file
state_data = pandas.read_csv("50_states.csv")

# keep track of the score
# score = 0
guessed_states = []

# create a turtle to do the dirty work
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.color("blue")

game_on = True
while game_on:
    # Get the user input
    if len(guessed_states) == 0:
        answer_state = screen.textinput(title="Guess a State", prompt="What is a state name?")
    else:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)}/{TOTAL_STATES} Stages Correct", prompt="What is another state name?"
        )
    # make the user input PascalCase
    if answer_state:
        answer_state = answer_state.title()
        # give a way to stop it
        if answer_state == "Exit":
            t.home()
            t.color("red")
            t.write(f"You quit with {len(guessed_states)}/{TOTAL_STATES} correct", align="center", font=ANNOUNCE_FONT)
            game_on = False
            # add a missing state for future learning
            missing_states = []
            for state in state_data.state.to_list():
                if state not in guessed_states:
                    missing_states.append(state)
            pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
            time.sleep(5)

    # if the guess is in the list, write it on the map, and update the score
    if answer_state in state_data.state.to_list():
        x = int(state_data[state_data.state == answer_state].x)
        y = int(state_data[state_data.state == answer_state].y)
        t.goto(x, y)
        t.write(answer_state, align="center", font=SCORE_FONT)
        guessed_states.append(answer_state)
    # The game is finished in this case.
    if len(guessed_states) == 50:
        t.home()
        t.color("Green")
        t.write("You got all 50 states!", align="center", font=ANNOUNCE_FONT)
        game_on = False


# turtle.mainloop()
# screen.exitonclick()


## stackoverflow get method to get the click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
