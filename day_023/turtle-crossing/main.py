"""main logic for the turtle game"""
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the player
player = Player()
# create the car manager
car_manager = CarManager()
# create the scoreboard
scoreboard = Scoreboard()

# handles the only key press action
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()

    scoreboard.update_score()
    car_manager.add_car()
    car_manager.move_cars()
    car_manager.clean_up()

    for car in car_manager.cars:
        # check the collision (game over criteria)
        lose = player.colide_with_car(car)
        if lose:
            # print the game over wording
            scoreboard.game_over()
            game_is_on = False

    # check the winning criteria
    win = player.check_win()
    if win:
        scoreboard.add_score()
        player.next_stage()
        SLEEP_TIME *= 0.9


screen.exitonclick()
