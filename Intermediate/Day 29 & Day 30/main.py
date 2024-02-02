import json
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def passwd_gen():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    passwd_input.insert(0,password)


# -------------------------------- SEARCH ---------------------------------- #

def search():
    try:
        with open("data.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            passwd = data[website_input.get()]["passwd"]
            messagebox.showinfo(message=f"These are the details entered: \n"
                                                f"Email: {email} "
                                                f"\nPassword: {passwd}" )
        else:
            messagebox.showinfo(message="No details for the website exists. ")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():

    new_dict = {
        website_input.get(): {
            "email": email_input.get(),
            "passwd": passwd_input.get()
        }
    }

    if len(website_input.get()) == 0 or len(passwd_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \n"
                                                                          f"Email: {email_input.get()} "
                                                              f"\nPassword: {passwd_input.get()} \n"
                                                                          f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_dict,f,indent=2)
            else:
                data.update(new_dict)

                with open("data.json", "w") as f:
                    json.dump(data, f, indent=2)

            finally:
                website_input.delete(0, END)
                email_input.delete(0,END)
                passwd_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=224)
image = PhotoImage(file="logo.png")
canvas.create_image(100,112,image=image)
canvas.grid(row=1,column=1)

website_label = Label(text="Website:")
website_label.grid(row=3,column=0)

website_input = Entry()
website_input.grid(row=3,column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=4,column=0)

email_input = Entry()
email_input.grid(row=4,column=1)

passwd_label = Label(text="Password:")
passwd_label.grid(row=5,column=0)

passwd_input = Entry()
passwd_input.grid(row=5,column=1)

button_passwd = Button(text="Generate Password", command=passwd_gen)
button_passwd.grid(row=5,column=2)

button_add = Button(text="Add",width=20, command=add_data)
button_add.grid(row=7,column=1)

button_search = Button(text="Search", width=20, command=search)
button_search.grid(row=3,column=2)

window.mainloop()