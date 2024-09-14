from tkinter import filedialog, PhotoImage, Label, Scrollbar, Frame, Text, Button, Tk, GROOVE, WORD, END
from PIL import Image, ImageTk
from customtkinter import CTk, CTkFrame, CTkButton, CTkTextbox
import os
from stegano import lsb

window = CTk()
window.title("Steganography - Hide a Secret Text Message in an Image")
window.geometry("700x500+150+180")
window.resizable(False, False)
window.configure(fg_color="#2f4155")

filename = None
secret = None

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetype=(("PNG file", ".png"),
                                                    ("JPG File", "*.jpg"), ("All File", "*.txt")))
    img = Image.open(filename)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(filename, message)

def Show():
    global filename
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    global secret
    if secret:
        secret.save("hidden.png")

image_icon = PhotoImage(file='D:\\PythonProjects\\tkinter\\logo.png')
window.iconphoto(False, image_icon)

logo = PhotoImage(file='D:\\PythonProjects\\tkinter\\logo.png')
Label(window, image=logo, bg="#2f4155").place(x=10, y=0)

Label(window, text="CYBER SCIENCE", bg="#2f4155", fg="white", font="arial 25 bold").place(x=100, y=20)

f = Frame(window, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

f2 = Frame(window, bd=3, width=340, height=280, bg="white", relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f3 = Frame(window, bd=3, bg="#2f4155", width=320, height=100, relief=GROOVE)
f3.place(x=10, y=370)

Button(f3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(f3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)

f4 = Frame(window, bd=3, bg="#2f4155", width=320, height=100, relief=GROOVE)
f4.place(x=360, y=370)

Button(f4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(f4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(f4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

window.mainloop()
