import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

BEGIN_X_COR = 0
BEGIN_Y_COR = 0
SLEEP_TIME = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Day 20
# TODO1: create a snake body
snake = Snake()

# TODO4: put food on screen
food = Food()

# TODO3: Control the snake with keyboard
screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")

# TODO5: keep track of score
scoreboard = Scoreboard()

# TODO2: Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    # use the move function in the snake class
    snake.move()
    # update the scoreboard

    # Day 21
    # TODO4: put food on screen, and detect collision with food
    if snake.head.distance(food) < 15:
        # TODO5: keep track of score, and create a score board
        scoreboard.scored()
        food.refresh()
        snake.extend()
        SLEEP_TIME *= 0.9

    # TODO6: Detect collision with the wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset()

    # TODO7: Detect collision with the snake itself
    # if the head collides with any part of the snake body, trigger game over
    for block in snake.snake[3:]:
        if snake.head.distance(block) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
