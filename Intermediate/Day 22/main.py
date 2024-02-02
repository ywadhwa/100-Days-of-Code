from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle(-350)
paddle_r = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.position_reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.position_reset()
        scoreboard.r_point()

screen.exitonclick()