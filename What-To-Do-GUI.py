from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk # Import PIL for image handling
import random
import os

# Define view_window as a global variable
view_window = None

# Display the information about this GUI
def info():
    new_window = CTkToplevel(window)
    new_window.config(bg="black")
    new_window.geometry("500x500")
    new_window.attributes('-topmost', 'true')  # Ensure new_window is always on top

    CTkLabel(master=new_window, text="1. What is What-To-Do?", text_color="white", font=CTkFont("Permanent Marker", size=30, weight="bold")).pack(pady=10)
    CTkLabel(master=new_window, text="When a person has too much work to do and can't decide which work the person should do first, they can use What-To-Do to help prioritize their tasks.",
             text_color="white", font=CTkFont("Permanent Marker", size=15, weight="bold"), wraplength=400).pack(pady=10)

    CTkLabel(master=new_window, text="2. How to Use What-To-Do?", text_color="white", font=CTkFont("Permanent Marker", size=30, weight="bold")).pack(pady=10)
    CTkLabel(master=new_window, text="To use What-To-Do, simply enter your tasks into the entry field and click 'Add'. Your tasks will be saved to a list. When you're ready to decide which task to work on, click 'Draw' to randomly select a task from your list.",
             text_color="white", font=CTkFont("Permanent Marker", size=15, weight="bold"), wraplength=400).pack(pady=10)

    CTkLabel(master=new_window, text="3. Viewing and Removing Tasks", text_color="white", font=CTkFont("Permanent Marker", size=30, weight="bold")).pack(pady=10)
    CTkLabel(master=new_window, text="You can view your list of tasks by clicking 'View'. If you want to remove a task, enter the task into the entry field and click 'Remove'. To remove all tasks, enter 'All' into the entry field and click 'Remove'.",
             text_color="white", font=CTkFont("Permanent Marker", size=15, weight="bold"), wraplength=400).pack(pady=10)

# Add new task to the list
def add():
    global work_list
    task = str(work_entry.get())
    if task:
        work_list.append(task)
        work_entry.delete(0, END)
        save_work_list()

# Draws a random task from the list
def draw():
    if work_list:
        x = random.choice(work_list)
        generate_label.configure(text=x)
        work_list.remove(x)
        save_work_list()
    else:
        generate_label.configure(text="Nothing to do!")

# Display the list of tasks
def view():
    global view_window
    if not view_window or not view_window.winfo_exists():
        view_window = CTkToplevel(window)
        view_window.config(bg="black")
        view_window.attributes('-topmost', 'true')  # Ensure view_window is always on top

        for i in work_list:
            CTkLabel(view_window, text=i, text_color="white", bg_color='black', font=CTkFont("Permanent Marker", size=15)).pack(pady=5)

# Helps to save the work list on the computer
def save_work_list():
    with open("work_list.txt", "w") as file:
        for task in work_list:
            file.write(f"{task}\n")

# Load the work list
def load_work_list():
    if os.path.exists("work_list.txt"):
        with open("work_list.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    return []

# Remove the entered or all the tasks from the list
def remove():
    task = work_entry.get()
    if task == "All":
        work_list.clear()
    elif task in work_list:
        work_list.remove(task)
    work_entry.delete(0, END)
    save_work_list()

# Hover effect
def on_enter(e):
    if isinstance(e.widget, CTkButton) or isinstance(e.widget, CTkEntry):
        e.widget.configure(fg_color="lightblue")

# Hover effect
def on_leave(e):
    if isinstance(e.widget, CTkButton) or isinstance(e.widget, CTkEntry):
        e.widget.configure(fg_color="white")

# Main window setup
window = CTk()
window.title("What-To-Do! Now?")
window.geometry("600x500")

# Info Button
info_button = CTkButton(master=window, text="i", fg_color="crimson", text_color="black", command=info, corner_radius=12, width=5)
info_button.place(x=570, y=5)
info_button.bind("<Enter>", on_enter)
info_button.bind("<Leave>", on_leave)

#Logo
logo = PhotoImage(file = "D:\\PythonProjects\\Tkinter\\Logo1.png")
CTkLabel(master = window,text = "",image = logo).place(x = 365,y = 25)
# Main Label
main_label = CTkLabel(master=window, text="What-To-Do! Now :)", font=CTkFont("Comic Sans MS", size=30, weight="bold"), width=100, height=50, text_color="lightblue")
main_label.place(x=250, y=100)

# Load the work list from the file
work_list = load_work_list()

# Main Image at the side
image_path = "D:\\PythonProjects\\Tkinter\\Label.png"
loaded_image = CTkImage(Image.open(image_path), size=(200, 500))
background_label = CTkLabel(master=window, image=loaded_image, text="")
background_label.place(y=0, x=0)

# Work Entry :- can enter task for adding or removing
work_entry = CTkEntry(master=window, placeholder_text="Enter Your Task here.....", font=CTkFont("Permanent Marker", size=20), width=250, border_color="lightblue", fg_color="#121212", text_color="#BB86FC")
work_entry.place(x=275, y=200)
work_entry.bind("<Enter>", on_enter)
work_entry.bind("<Leave>", on_leave)

# Task adding Button
add_button = CTkButton(master=window, text="Add", width=75, corner_radius=10, command=add, fg_color="lightgreen", text_color="black", font=CTkFont("Permanent Marker", size=15))
add_button.place(x=275, y=250)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

# Remove button
remove_button = CTkButton(master=window, text="Remove", width=75, corner_radius=10, command=remove, fg_color="lightgreen", text_color="black", font=CTkFont("Permanent Marker", size=15))
remove_button.place(x=362, y=250)
remove_button.bind("<Enter>", on_enter)
remove_button.bind("<Leave>", on_leave)

# View Button
view_button = CTkButton(master=window, text="View", width=75, corner_radius=10, command=view, fg_color="lightgreen", text_color="black", font=CTkFont("Permanent Marker", size=15))
view_button.place(x=450, y=250)
view_button.bind("<Enter>", on_enter)
view_button.bind("<Leave>", on_leave)

# Label
draw_label = CTkLabel(master=window, text="You are gonna do :-", font=CTkFont("Permanent Marker", size=15, weight="bold"))
draw_label.place(x=250, y=325)

# Task generate label
generate_label = CTkLabel(master=window, text="Nothing", font=CTkFont("Permanent Marker", size=15, weight="bold"))
generate_label.place(x=400, y=325)

# Generate button
generate_button = CTkButton(master=window, text="Draw", width=100, corner_radius=10, command=draw, fg_color="lightgreen", text_color="black", font=CTkFont("Permanent Marker", size=15))
generate_button.place(x=450, y=375)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

window.mainloop()
