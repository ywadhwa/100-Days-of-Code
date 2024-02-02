from turtle import Turtle
import random
colours = ["blue","yellow","orange","purple","black","red"]
move_inc = 3

class Car:
    def __init__(self):
        self.all_car = []
        self.move_distance = 5
    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            car = Turtle()
            random_c = random.choice(colours)
            car.color(random_c)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.penup()
            y = random.randint(-250,250)
            car.goto(300,y)
            self.all_car.append(car)

    def move(self):
        for car in self.all_car:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += move_inc

