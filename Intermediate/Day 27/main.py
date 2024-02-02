from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=200, height=200)
window.config(padx=20,pady=20)

input_miles = Entry(width=5)
input_miles.grid(column=2,row=1)

label1 = Label(text="Miles")
label1.grid(column=3,row=1)

label2 = Label(text="is equal to")
label2.grid(column=1,row=2)

label3 = Label(text="Km")
label3.grid(column=3,row=2)

label_km = Label(text="")
label_km.grid(column=2,row=2)

def button_clicked():
    label_km.config(text=int(int(input_miles.get())*1.6))

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2,row=3)





window.mainloop()