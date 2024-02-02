import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", font=(FONT_NAME,25,"bold"), foreground= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", font=(FONT_NAME,25,"bold"), foreground= PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME,25,"bold"), foreground= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(time):

    count_min = math.floor(time/60)
    count_sec = time % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_time()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

button_start = Button(text="Start",highlightthickness=0,command=start_time)
button_start.grid(row=2,column=0)

button_reset = Button(text="Reset",highlightthickness=0,command=reset_time)
button_reset.grid(row=2,column=2)

label = Label(text="Timer",foreground=GREEN,font=(FONT_NAME,25,"bold"),background=YELLOW,)
label.grid(row=0,column=1)

check_mark = Label( foreground=GREEN, background=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()