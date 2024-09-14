from tkinter import *

window = Tk()
window.geometry('1000x500')
window.title('Bill Management')
window.resizable(False, False)

Label(text='Bill Management', bg='black', fg='white', font=('calibri', 33), width='300', height='2').pack()

#def Buttons

def reset():
    entry_dosa.delete(0,END)
    entry_cookie.delete(0,END)
    entry_Tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_eggs.delete(0,END)


def total():
    try:a1 = int(dosa.get())
    except: a1 = 0

    try:a2 = int(cookies.get())
    except: a2 = 0

    try:a3 = int(Tea.get())
    except: a3 = 0

    try:a4 = int(coffee.get())
    except: a4 = 0

    try:a5 = int(juice.get())
    except: a5 = 0

    try:a6 = int(pancakes.get())
    except: a6 = 0

    try:a7 = int(eggs.get())
    except: a7 = 0

    #define cost of each item per quantity
    c1 = 60*a1
    c2 = 30*a2
    c3 = 7*a3
    c4 = 100*a4
    c5 = 20*a5
    c6 = 15*a6
    c7 = 7*a7

    lbl_total = Label(bill,font=('aria',20,'bold'),text = 'Total',width = 16,fg='lightyellow',bg='black')
    lbl_total.place(x= 10, y = 50)

    entry_total = Entry(bill,font=('aria',20,'bold'),textvariable=total_bill,bd=6,width=15,bg= 'lightgreen')
    entry_total.place(x = 20,y = 100)

    totalcost = c1 + c2 + c3 +c4 + c5 + c6 +c7
    string_bill = 'Rs.',str('%.2f' %totalcost)
    total_bill.set(string_bill)


# Menu Card
Menu_Card = Frame(window, bg='lightgreen', highlightbackground='black', highlightthickness=1, width=300, height=370)
Menu_Card.place(x=10, y=118)
Label(Menu_Card, text='Menu', font=('gabriola', 40, 'bold'), fg='black', bg='lightgreen').place(x=80, y=0)

Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Dosa.........Rs.60/Plate', fg='black', bg='lightgreen').place(x=10, y=80)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Cookies......Rs.30/Plate', fg='black', bg='lightgreen').place(x=10, y=110)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Tea..........Rs.7/Cup', fg='black', bg='lightgreen').place(x=10, y=140)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Coffee.......Rs.100/Cup', fg='black', bg='lightgreen').place(x=10, y=170)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Juice........Rs.20/Plate', fg='black', bg='lightgreen').place(x=10, y=200)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Pancakes.....Rs.15/Pack', fg='black', bg='lightgreen').place(x=10, y=230)
Label(Menu_Card, font=('Lucida Calligraphy', 15, 'bold'), text='Eggs.........Rs.7/egg', fg='black', bg='lightgreen').place(x=10, y=260)

# Entry Work
Entry_Work = Frame(window, bd=5, height=370, width=300, relief=RAISED)
Entry_Work.place(x=325, y=118)

dosa = StringVar()
cookies = StringVar()
Tea = StringVar()
coffee = StringVar()
juice = StringVar()
pancakes = StringVar()
eggs = StringVar()
total_bill = StringVar()

# Labels and Entries
Label(Entry_Work, font=('aria', 20, 'bold'), text='Dosa', width=12, fg='blue4').grid(row=1, column=0)
entry_dosa = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=dosa, bd=6, width=8, bg='lightpink', justify='right')
entry_dosa.grid(row=1, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Cookies', width=12, fg='blue4').grid(row=2, column=0)
entry_cookie = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=cookies, bd=6, width=8, bg='lightpink', justify='right')
entry_cookie.grid(row=2, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Tea', width=12, fg='blue4').grid(row=3, column=0)
entry_Tea = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=Tea, bd=6, width=8, bg='lightpink', justify='right')
entry_Tea.grid(row=3, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Coffee', width=12, fg='blue4').grid(row=4, column=0)
entry_coffee = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=coffee, bd=6, width=8, bg='lightpink', justify='right')
entry_coffee.grid(row=4, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Juice', width=12, fg='blue4').grid(row=5, column=0)
entry_juice = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=juice, bd=6, width=8, bg='lightpink', justify='right')
entry_juice.grid(row=5, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Pancakes', width=12, fg='blue4').grid(row=6, column=0)
entry_pancakes = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=pancakes, bd=6, width=8, bg='lightpink', justify='right')
entry_pancakes.grid(row=6, column=1)

Label(Entry_Work, font=('aria', 20, 'bold'), text='Eggs', width=12, fg='blue4').grid(row=7, column=0)
entry_eggs = Entry(Entry_Work, font=('aria', 20, 'bold'), textvariable=eggs, bd=6, width=8, bg='lightpink', justify='right')
entry_eggs.grid(row=7, column=1)



#Buttons

reset_button = Button(Entry_Work, text='Reset', command=reset, fg='black', bg='lightblue', font=('arial', 16, 'bold'), bd=5)
reset_button.grid(row=8, column=0)

total_button = Button(Entry_Work,text = 'Total',command = total,fg = 'black',bg = 'lightblue',font = ('arial',16,'bold'),bd = 5)
total_button.grid(row = 8,column = 1)


#BILL
bill = Frame(window,bg = 'lightyellow',highlightbackground= 'black',highlightthickness = 1,width=300,height = 370)
bill.place(x= 690,y = 118)

Bill = Label(bill,text = 'Bill',font=('calibri',20),bg = 'lightyellow')
Bill.place(x = 120,y = 10)


window.mainloop()
