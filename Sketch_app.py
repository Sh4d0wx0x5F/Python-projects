from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.speed("normal")
    tim.forward(10)

def move_backward():
    tim.speed("normal")
    tim.back(10)

def counter_clockwise():
    tim.speed("slowest")
    tim.left(10)

def clockwise():
    tim.speed("slowest")
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear)
screen.exitonclick()
