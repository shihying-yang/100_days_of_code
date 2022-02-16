### This code will not work in repl.it as there is no access to the colorgram package here. ###
## We talk about this in the video tutorials ##
"""Requirement: 10 x 10 dots, each dot is 20, and space apart by 50"""

import random
import turtle as t

t.colormode(255)

START_POSITION = -250
DOT_COUNT = 10
DOT_SIZE = 20
DOT_DISTANCE = 50

## code block to get the color pallet ##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     rgb_color = color.rgb
#     r = rgb_color.r
#     g = rgb_color.g
#     b = rgb_color.b
#     if r < 240 and g < 240 and b < 240:
#         rgb_colors.append((r, g, b))

# print(rgb_colors)

color_list = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]


tim = t.Turtle()


def goto_start_position():
    """moves the turtle to the appropriate start position"""
    tim.penup()
    tim.setx(START_POSITION)
    tim.sety(START_POSITION)
    tim.setheading(0)
    tim.pendown()


def goto_next_row():
    """moves the turtle to the next row"""
    tim.penup()
    tim.setx(START_POSITION)
    tim.setheading(90)
    tim.forward(DOT_DISTANCE)
    tim.setheading(0)
    tim.pendown()


tim.speed("fastest")

goto_start_position()
for _ in range(DOT_COUNT):
    for _ in range(DOT_COUNT):
        tim.dot(DOT_SIZE, random.choice(color_list))
        tim.penup()
        tim.forward(DOT_DISTANCE)
        tim.pendown()
    goto_next_row()


screen = t.Screen()
screen.exitonclick()
