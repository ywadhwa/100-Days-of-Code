import random
from turtle import *

turtle1 = Turtle()

#Draw a Square
#for i in range(4):
#    turtle1.forward(50)
#    turtle1.left(90)

#Draw a dashed line

#for i in range(15):
#    turtle1.forward(5)
#    turtle1.penup()
#    turtle1.forward(5)
#    turtle1.pendown()


#Drawing different shapes

from random import *

def change_color():
    R = random()
    G = random()
    B = random()

    turtle1.color(R,G,B)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#def draw_shape(num_sides):
#    for i in range(num_sides):
#        #change_color()
#        turtle1.forward(50)
#        turtle1.right(360 / num_sides)

#for i in range(3,11):
#    turtle1.color(choice(colors))
#    draw_shape(i)

#Draw random shapes
#directions = [0,90,180,270]

#for i in range(200):
#    change_color()
#    turtle1.width(width=10)
#    turtle1.speed('fast')
#    turtle1.forward(30)
#    turtle1.setheading(choice(directions))

def spirograph(gap):
    for i in range(int(360/gap)):
        change_color()
        turtle1.speed('fastest')
        turtle1.circle(radius=50)
        turtle1.setheading(turtle1.heading() + gap)

spirograph(5)

screen = Screen()
screen.exitonclick()

