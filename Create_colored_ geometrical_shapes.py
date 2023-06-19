from turtle import Turtle, Screen
import random

timmy = Turtle()

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    tim.color(color)

sides = 3
timmy.pensize(10)
for i in range(7):
    change_color()
    for side in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)
    sides += 1

screen = Screen()
screen.exitonclick()
