
# --------------------------Flash Card Creation ------------------------#

import pandas as pd
import random

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    flash_data = pd.read_csv("data/french_words.csv")
    dict_card = flash_data.to_dict(orient="records")
else:
    dict_card = data.to_dict(orient="records")


card_dict = {}
def button_action():
    global flip_timer,card_dict
    window.after_cancel(flip_timer)
    canvas1.itemconfig(image_item, image=image_before)
    canvas1.itemconfig(title_text,text="French",fill='black')
    card_dict = random.choice(dict_card)
    canvas1.itemconfig(word_text,text=card_dict['French'],fill='black')
    flip_timer = window.after(3000, flip_card)

# ----------------------------- Flip Cards ------------------------#

def flip_card():
    canvas1.itemconfig(title_text,text="English",fill='white')
    canvas1.itemconfig(image_item,image=image_after)
    canvas1.itemconfig(word_text,text=card_dict['English'],fill='white')

# --------------------------Save Progress -------------------------#

def is_known():
    dict_card.remove(card_dict)
    data = pd.DataFrame(dict_card)
    data.to_csv('./data/words_to_learn.csv', index=False)
    button_action()


# -----------------------------------UI-------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
flip_timer = ""

from tkinter import *

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas1 = Canvas(width=800, height=526)
image_before = PhotoImage(file='./images/card_front.png')
image_after = PhotoImage(file='./images/card_back.png')

image_item = canvas1.create_image(400,263,image=image_before)
canvas1.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas1.grid(row=0,column=0,columnspan=2)

flip_timer = window.after(3000, flip_card)

title_text = canvas1.create_text(400,150,text="Title",font=(FONT_NAME,40,"italic"))
word_text = canvas1.create_text(400,263,text="Word",font=(FONT_NAME,60,"bold"))

image2 = PhotoImage(file='./images/wrong.png')
button1 = Button(image=image2,highlightthickness=0,command=button_action)
button1.grid(row=1,column=0)

image3 = PhotoImage(file='./images/right.png')
button2 = Button(image=image3,highlightthickness=0,command=is_known)
button2.grid(row=1,column=1)


button_action()

window.mainloop()
