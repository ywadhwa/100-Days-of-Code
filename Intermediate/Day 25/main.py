from turtle import Turtle,Screen
import pandas as pd
import time

turtle = Turtle()
screen = Screen()

screen.screensize(canvwidth=800,canvheight=600)
screen.title("Name the State")

screen.register_shape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

screen.tracer(0)

states = pd.read_csv("50_states.csv")
df_states = pd.DataFrame(states)

game_on = True

def write_state_name(turtle, state_name, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(state_name, align="center", font=("Arial", 12, "normal"))
    turtle.goto(0,0)

correct_guess = []
score = 0

while len(correct_guess) < 50:
    time.sleep(0.1)
    screen.update()
    user_input = screen.textinput(f" {score}/50 States Correct","State Name:")

    if user_input in df_states['state'].values:
        guessed_state = df_states[df_states['state'] == user_input].iloc[0]
        x,y = guessed_state['x'],guessed_state['y']
        write_state_name(turtle,user_input,x,y)
        score += 1
        correct_guess.append(user_input)
    elif user_input == "Exit":
        with open("missing_states.csv", "w") as file:
            for state in df_states['state'].values:
                if state not in correct_guess:
                    file.write(state + "\n")
        break
    else:
        pass

screen.exitonclick()


