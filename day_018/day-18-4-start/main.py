import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

tim.pensize(10)
# tim.speed(0)
tim.speed("fastest")

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    # tim.right(random.choice(directions))
    tim.setheading(random.choice(directions))
    tim.forward(30)


screen = t.Screen()
screen.exitonclick()
