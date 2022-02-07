import turtle as t
from random import choice

# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "black"]
colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########


def draw_shape(num_sides):
    """draws a shape with the given number of sides

    :param num_sides: number of sides
    :type num_sides: int
    """
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for sides in range(3, 11):
    color = choice(colors)
    colors.remove(color)
    tim.color(color)
    draw_shape(sides)


screen = t.Screen()
screen.exitonclick()
