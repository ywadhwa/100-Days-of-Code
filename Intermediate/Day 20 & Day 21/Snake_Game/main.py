from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=1000,height=1000)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
sboard = Scoreboard()

screen.listen()


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        sboard.scorecount()
        snake.extend()

    if snake.segments[0].xcor() > 450 or snake.segments[0].xcor() < -450 or snake.segments[0].ycor() > 450 or snake.segments[0].ycor() < -450:
        sboard.gameover()
        game_on = False

    for head in snake.segments[1:]:
        if snake.segments[0].distance(head) < 10:
            game_on = False
            sboard.scorecount()


screen.exitonclick()