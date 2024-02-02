import random
from turtle import Turtle,Screen

race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

y = -100

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230,y)
    y += 35
    all_turtles.append(turtle)

if user_bet:
    race_on = True

while race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            winner = t.pencolor()
            race_on = False
        distance = random.randint(0, 10)
        t.forward(distance)

if user_bet == winner:
    print("You won")
else:
    print(f"You lost. The winner was {winner}")

screen.exitonclick()