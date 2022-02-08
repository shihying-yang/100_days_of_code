"""Create an etch-a-sketch simulator """
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# w = forward, s = backward, a = counter-clockwise, d = clockwise, c = clear


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_left)
screen.onkeypress(key="a", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
