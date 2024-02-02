from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self,position):
        turtle1 = Turtle()
        turtle1.color("white")
        turtle1.shape("square")
        turtle1.penup()
        turtle1.goto(position)
        self.segments.append(turtle1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_no - 1].xcor()
            y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
             self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)




