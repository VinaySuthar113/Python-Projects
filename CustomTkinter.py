from customtkinter import *
from textblob import TextBlob

window = CTk()
window.geometry("700x500")
window.title("Spelling Checker")
set_appearance_mode("Dark")
window.resizable(False,False)

def check():
    word = entry.get()
    a = TextBlob(word)
    right = str(a.correct())
    cs = CTkLabel(master = main_frame,text = "Correct Spelling is :- ", font = ("poppins",20)).place(x=100,y = 300)
    spell.configure(text = right)
    
main_frame = CTkFrame(master = window,height = 400,width = 600,corner_radius = 25)
main_frame.pack(pady = 40)

Main_Label = CTkLabel(master = main_frame,text = "Spelling Checker" ,font = ("poppins",35,"bold"),text_color = ("white"),corner_radius = 5)
Main_Label.place(x = 180,y = 50)

entry = CTkEntry(master = main_frame,placeholder_text = "Enter Your Spelling here.....",fg_color = "black",width = 400,font = ("poppins",15,"bold"))
entry.place(x = 120,y = 150)
button = CTkButton(master = main_frame,command = check,text = "Check",corner_radius = 50,width = 100,hover_color = "white",text_color = "black",font = ("poppins",15,"italic")).place(x = 270 , y = 220)

spell = CTkLabel(master = main_frame,font = ("poppins",20),text = "")
spell.place(x = 300,y = 300)

window.mainloop()
