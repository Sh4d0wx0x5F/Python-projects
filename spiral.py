import turtle as t
import random

tim = t.Turtle()

t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    tim.color(color)

tim.speed('fastest')
def spacing(space):
    for _ in range(int(360 / space)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + space)

spacing(4)

screen = t.Screen()
screen.exitonclick()
