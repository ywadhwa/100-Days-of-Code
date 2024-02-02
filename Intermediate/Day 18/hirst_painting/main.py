import turtle

import colorgram
from turtle import *
import random

colors = colorgram.extract('hirst_painting.jpg',10)

c = []

for i in colors:
    r = i.rgb.r
    b = i.rgb.b
    g = i.rgb.g
    new_color = (r,g,b)
    c.append(new_color)

print(c)

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.speed('fastest')
turtle.colormode(255)
for i in range(1,50):
    turtle1.dot(20,random.choice(c))
    turtle1.penup()
    turtle1.forward(50)
    turtle1.pendown()

    if i % 10 == 0:
        turtle1.setheading(90)
        turtle1.penup()
        turtle1.forward(50)
        turtle1.setheading(180)
        turtle1.forward(500)
        turtle1.setheading(0)
        turtle1.pendown()

screen = Screen()
screen.exitonclick()

#print(c)

