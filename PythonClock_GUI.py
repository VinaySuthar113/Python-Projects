from tkinter import *
from customtkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S")
    time_label.configure(text = time_string)

    day_string = strftime("%A")
    day_label.configure(text = day_string)

    date_string = strftime("%B %d, %Y")
    date_label.configure(text = date_string)
            
    window.after(1000,update)

window = CTk()
window.title("My Clock")
window.resizable(False,False)


time_label = CTkLabel(master = window,text = "" ,font = ("Arial", 50),text_color = "#00ff00",bg_color = "black")
time_label.pack()

day_label = CTkLabel(master = window,text = "" ,font = ("Ink Free", 25))
day_label.pack()

date_label = CTkLabel(master = window,text = "" ,font = ("Ink Free", 30))
date_label.pack()

update()

window.mainloop()
