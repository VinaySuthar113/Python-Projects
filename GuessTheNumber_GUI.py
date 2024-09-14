from tkinter import *
import random
import os

def start():
    global Number
    global count
    global temp_Name
    
    Name_label.config(text="Enter your Guess between 1 to 100")
    Start_Button.config(text="Check", command=check)
    temp_Name = str(Name_Entry.get())
    Name_Entry.delete(0, END)
    Number = random.randint(1, 100)
    count = 1

def check():
    global count
    global Highest_Scorer
    global Highest_Score
    
    try:
        guess = int(Name_Entry.get())
        
        if guess == Number:
            if count < Highest_Score:
                Name_label.config(text="YaY! you are correct :)")
                Highest_Score = count
                Highest_Scorer = temp_Name
                Highest_Score_label.config(text=Highest_Score)
                Highest_Name_label.config(text=Highest_Scorer)
                save_highest_score()
        elif guess > Number:
            Name_label.config(text="Your Guess is Too Big :|")
            count += 1
        elif guess < Number:
            Name_label.config(text="Your Guess is Too Small :|")
            count += 1
        elif guess > 100 or guess < 1:
            Name_label.config(text="You are out of range :(")
            count += 1

    except ValueError:
        Name_label.config(text="ERROR! Please enter a valid number :(")

def save_highest_score():
    with open("highest_score.txt", "w") as file:
        file.write(f"{Highest_Score}\n{Highest_Scorer}")

def load_highest_score():
    global Highest_Score
    global Highest_Scorer
    
    if os.path.exists("highest_score.txt"):
        with open("highest_score.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                Highest_Score = int(lines[0].strip())
                Highest_Scorer = lines[1].strip()

window = Tk()
window.title("Guess The Number")
window.geometry("400x500")
window.config(bg="LightBlue")

MainLabel2 = Label(window, text="Guess the Number?", bg='black', font=("caliber", 30, "bold"), fg="white", width=100).pack()

mainFrame = Frame(window, bg='lightblue')
mainFrame.pack(pady=50)

Highest_Scorer = "No Name"
Highest_Score = 100000
count = 1

load_highest_score()

Name_label = Label(mainFrame, text="Please Enter Your Name!", font=("claiber", 15, "bold"), bg="lightBlue")
Name_label.grid(row=0, column=0, pady=15)
Name_Entry = Entry(mainFrame, font=("claiber", 25, "bold"), relief=SUNKEN, bd=5, bg="brown")
Name_Entry.grid(row=1, column=0)
Start_Button = Button(mainFrame, bg="red", text="Start", fg="Black", relief=RAISED, command=start, width=7, height=1, bd=5, font=("Arial", 15, "bold"))
Start_Button.grid(row=2, column=0, pady=30)
Highest_label = Label(mainFrame, text="Highest Scorer:-", font=("claiber", 15, "bold"), bg="lightblue")
Highest_label.grid(row=3, column=0)
Highest_Name_label = Label(mainFrame, text=Highest_Scorer, font=("claiber", 15, "bold"), bg="lightblue")
Highest_Name_label.grid(row=4, column=0)
Highest_Score_label = Label(mainFrame, text=Highest_Score, font=("claiber", 15, "bold"), bg="lightblue")
Highest_Score_label.grid(row=5, column=0)

window.mainloop()
