"""main game function in here"""

import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1

# TODO1: create a screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

# TODO2: create a paddle (and add move function)
l_paddle = Paddle("left", SCREEN_HEIGHT)
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

# TODO3: handle another paddle
r_paddle = Paddle("right", SCREEN_HEIGHT)
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

# TODO4: create a ball (and add move function)
ball = Ball()

# TODO8: Keep score
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    # TODO4: add ball move function
    ball.move()

    # TODO5: detect collision between the ball and the wall
    if ball.xcor() < (-1 * SCREEN_WIDTH / 2) + 25 or ball.xcor() > (SCREEN_WIDTH / 2) - 25:
        ball.bounce_left_right()
    if ball.ycor() < (-1 * SCREEN_HEIGHT / 2) + 25 or ball.ycor() > (SCREEN_HEIGHT / 2) - 25:
        ball.bounce_up_down()

    # TODO6: detect collision between the ball and the paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() > (-1 * SCREEN_WIDTH / 2) + 38) or (
        ball.distance(r_paddle) < 50 and ball.xcor() < (SCREEN_WIDTH / 2) - 38
    ):
        ball.bounce_left_right()
        SLEEP_TIME *= 0.9

    # TODO7: detect paddle miss
    if ball.xcor() > (SCREEN_WIDTH / 2) - 20:
        # TODO8: Keep score
        scoreboard.increase_score("left")
        ball.reset_position()
        SLEEP_TIME = 0.1
        # scoreboard.reset_game()
        time.sleep(1)

    if ball.xcor() < (-1 * SCREEN_WIDTH / 2) + 20:
        scoreboard.increase_score("right")
        ball.reset_position()
        SLEEP_TIME = 0.1
        # scoreboard.reset_game()
        time.sleep(1)


screen.exitonclick()
