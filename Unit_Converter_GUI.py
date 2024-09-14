from tkinter import *

def submit():
    if From_option.get() ==  To_option.get():
        value = DataEntry.get()
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Gm' and  To_option.get() == 'Mg':
        value = format(int(DataEntry.get())*1000)
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Gm' and  To_option.get() == 'Kg':
        value = format(int(DataEntry.get())/1000)
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Mg' and  To_option.get() == 'Kg':
        value = format(int(DataEntry.get())/1000000)
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Mg' and  To_option.get() == 'Gm':
        value = format(int(DataEntry.get())/1000)
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Kg' and  To_option.get() == 'Gm':
        value = format(int(DataEntry.get())*1000)
        ConverterEntry.insert(0,value)
    elif From_option.get() == 'Kg' and  To_option.get() == 'Mg':
        value = format(int(DataEntry.get())*1000000)
        ConverterEntry.insert(0,value)
    
    
    
window = Tk()
window.geometry("500x350")
window.config(bg='lightgreen')
window.title('Unit Converter')
window.resizable(False, False)

Main_Label = Label(window, text='Unit Converter', bg='black', fg='white', font=('calibri', 25), pady=10)
Main_Label.pack(fill=X)

Main_Frame = Frame(window, bg='lightgreen')
Main_Frame.pack(pady=20, padx=5, fill=X)

DataLabel = Label(Main_Frame, text='Current Unit Data:-', bg='lightgreen',font=('calibri',12,'bold'))
DataLabel.grid(row=0, column=0, padx=15, pady=10, sticky=E)

DataEntry = Entry(Main_Frame, font=('Arial', 15), relief=SUNKEN, width=25, bd=5,bg = 'lightyellow')
DataEntry.grid(row=0, column=1, padx=15, pady=10)

ConverterLabel = Label(Main_Frame, text='Converted Unit Data:-', bg='lightgreen',font=('calibri',12,'bold'))
ConverterLabel.grid(row=1, column=0, padx=15, pady=10, sticky=E)

ConverterEntry = Entry(Main_Frame, font=('Arial', 15), relief=SUNKEN, width=25, bd=5,bg = 'lightyellow')
ConverterEntry.grid(row=1, column=1, padx=15, pady=10)


#from

# Dropdown menu options
From_label1 = Label(Main_Frame,text = 'From:',bg = 'lightgreen',font=('calibri',12,'bold'))
From_label1.grid(row=2, column=0, padx=15, pady=10)
options = ["Kg", "Gm", "Mg"]

# Variable to store the selected option
From_option = StringVar()
From_option.set("FROM")  # Set the default option

# Create the dropdown menu
dropdown1 = OptionMenu(Main_Frame, From_option, *options)
dropdown1.grid(row=2, column=1, padx=15, pady=10)

#To

# Dropdown menu options
From_label2 = Label(Main_Frame,text = 'To:',bg = 'lightgreen',font=('calibri',12,'bold'))
From_label2.grid(row=3, column=0, padx=15, pady=10)
options = ["Kg", "Gm", "Mg"]

# Variable to store the selected option
To_option = StringVar()
To_option.set('TO')  # Set the default option

# Create the dropdown menu
dropdown2 = OptionMenu(Main_Frame, To_option, *options)
dropdown2.grid(row=3, column=1, padx=15, pady=10)


submit_button = Button(Main_Frame,text = 'submit',command = submit,bg = 'lightpink',fg = 'blue',relief = RAISED)
submit_button.grid(row = 4,column =0 , columnspan = 2,pady = 5)
window.mainloop()
