from turtle import Turtle,Screen

turtle1 = Turtle()
screen = Screen()

def forward():
    turtle1.forward(50)

def backward():
    turtle1.back(50)

def counter_clock():
    turtle1.left(45)

def clock():
    turtle1.right(45)

def clear():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
