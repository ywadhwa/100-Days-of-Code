from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 270)
        self.write(f"Level: {self.level} ",align="left", font=("Courier", 12, "normal"))

    def level_update(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over.",align="center", font=("Courier", 12, "normal"))