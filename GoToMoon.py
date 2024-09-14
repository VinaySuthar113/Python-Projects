from tkinter import StringVar,messagebox
from customtkinter import *
from PIL import Image, ImageTk

def submit():
    name =  name_entry.get()
    Class = option2.get()
    Station =  option1.get()
    messagebox.showinfo(title = "Ride Confirmation",message = f"One {Class} Ticket for {name} has been booked from the {Station}")
    
window = CTk()
window.title("GoToMoon")
window.geometry("350x575")
window.resizable(False, False)
window.configure(fg_color="#272B30")

# Use PIL to open the image and handle transparency
image_path = "D:\\PythonProjects\\Tkinter\\space_man.png"
image = Image.open(image_path)
image = image.convert("RGBA")  # Ensure the image has an alpha channel
photo_image = ImageTk.PhotoImage(image)

# Use the photo image in the CTkLabel
image_label = CTkLabel(master=window, image=photo_image, text="", fg_color="transparent")
image_label.place(x=0, y=0)

options1 = ["Indian Space Research Station (ISRS)", "National Aeronautics and Space Station (NASS)"]
option1 = StringVar()
option1.set("Select Station")  # Set the initial display text

dropdown1 = CTkOptionMenu(master=window, variable=option1, bg_color="#2A314D", dropdown_fg_color="black",fg_color="#1e1e1e", button_hover_color="#2B214F", corner_radius=10, button_color="black",values=options1, width=300)
dropdown1.place(x=25, y=350)

name_entry = CTkEntry(master=window,placeholder_text = "Enter Name...", width=150, corner_radius=5, fg_color="transparent",border_width = 2,border_color = "#2F454F")
name_entry.place(x=10, y=425)

options2 = ['A class', 'B class', 'C class']
option2 = StringVar()
option2.set("Select Class")  # Set the initial display text for the second dropdown

dropdown2 = CTkOptionMenu(master=window, variable=option2, values=options2, width=150,fg_color = "#1e1e1e", button_hover_color="#2B214F", corner_radius=10, button_color="black")
dropdown2.place(x=185, y=425)

submit_button = CTkButton(master=window, text="Submit", width=120, fg_color="transparent", border_width=2, command=submit)
submit_button.place(x=110, y=500)

window.mainloop()
