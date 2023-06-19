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


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed('fast')
game = True
while game:
    change_color()
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
