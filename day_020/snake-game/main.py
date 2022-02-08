from turtle import Screen
import time
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


# TODO3: Control the snake with keyboard
screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")


# TODO2: Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    # use the move function in the snake class
    snake.move()


# Day 21
# TODO4: put food on screen, and detect collision with food


# TODO5: keep track of score, and create a score board


# TODO6: Detect collision with the wall


# TODO7: Detect collision with the snake itself


screen.exitonclick()
