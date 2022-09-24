from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "green", "blue", "orange", "yellow", "black"]

turtles = []
y = -125

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-225, y)
    y += 50
    turtles.append(new_turtle)


race_on = False

if user_input:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() >= 220:
            race_on = False
            if user_input.lower() == turtle.pencolor():
                print(f"You WIN!!!. {turtle.pencolor()} turtle is winner")

            else:
                print(f"You LOSE!!!. {turtle.pencolor()} turtle is winner")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
