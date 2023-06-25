from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter the color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]
all_tim = []

for tim in range(0, 6):
    tims = Turtle(shape="turtle")
    tims.color(color[tim])
    tims.penup()
    tims.goto(x=-250, y=y_position[tim])
    all_tim.append(tims)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_tim:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner")
        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)



screen.exitonclick()
