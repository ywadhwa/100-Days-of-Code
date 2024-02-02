from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_cord):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.paddle_position(x_cord)
        self.speed("fast")

    def paddle_position(self,x_cord):
        self.goto(x_cord, 0)

    def up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def down(self):
        self.goto(self.xcor(),self.ycor()-30)