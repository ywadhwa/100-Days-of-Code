from turtle import Screen,Turtle
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screen.screensize(canvwidth=600,canvheight=600)
screen.listen()

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")

game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for c in car.all_car:
        if c.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        player.goto(0, -280)
        car.level_up()
        scoreboard.level_update()

screen.exitonclick()