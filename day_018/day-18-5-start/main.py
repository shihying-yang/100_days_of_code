import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    """create a random color from RGB 255 value

    :return: [description]
    :rtype: [type]
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

circle_count = 75
tim.speed("fastest")

for _ in range(circle_count):
    angle = 360 / circle_count
    tim.color(random_color())
    tim.circle(100)
    tim.left(angle)


screen = t.Screen()
screen.exitonclick()
