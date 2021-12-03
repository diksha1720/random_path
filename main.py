import turtle
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


direction = [90, 180, 270, 0]
tim = turtle.Turtle()
tim.pensize(10)
tim.speed("fastest")
for _ in range(300):
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(30)
screen = turtle.Screen()
screen.exitonclick()
