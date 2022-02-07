import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

tim.shape("turtle")
tim.color("turquoise")

for _ in range(20):
    tim.forward(10)
    # tim.pencolor("white")
    tim.penup()
    tim.forward(10)
    # tim.pencolor("turquoise")
    tim.pendown()

screen = t.Screen()
screen.exitonclick()
