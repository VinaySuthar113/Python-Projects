from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry('600x600')
window.title("Notepad")
window.resizable(False,False)
window.config(bg = 'lightblue')


def save_file():
    open_file = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt')
    if open_file is None:
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode = 'r',filetype = [('text files'),'*.txt'])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)
    
entry = Text(window,height = 33,width = 72,wrap = WORD)
entry.place(x = 10,y = 60)

b1 = Button(window,width = 20,height = 2,bg = 'lightgreen',text = 'save file',font = ('airal',10, 'bold'),command = save_file,relief = RAISED,bd = 5).place(x=100,y = 5)
b2 = Button(window,width = 20,height = 2,bg = 'lightgreen',text = 'open file',font = ('airal',10, 'bold'),command = open_file,relief = RAISED,bd = 5).place(x=300,y = 5)

window.mainloop()
