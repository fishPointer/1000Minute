from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter.ttk import Progressbar

global start_hours
global start_minutes
start_hours = 5
start_minutes = 0

root = Tk()
root.title("1000 Minutes")
root.geometry("700x300")
img = PhotoImage(file='/home/eein/Documents/Lab/Code/1000Minute/skull.png')
root.call('wm', 'iconphoto', root._w, img)

var = IntVar()
var.set(5)

var2 = IntVar()
var.set(0)

optionslist = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
]   

minutelist = [
    00,
    10,
    20,
    30,
    40,
    50,
]

def savechanges():
    global start_hours
    global start_minutes
    start_hours = var.get()
    start_minutes = var2.get()

def changesettime():
    top = Toplevel()
    top.title("Select New Starting Time")
    top.geometry("300x300")
    img = PhotoImage(file='/home/eein/Documents/Lab/Code/1000Minute/skull.png')
    root.call('wm', 'iconphoto', top._w, img)
    lbl = Label(top, font=('calibri', 16, 'bold'), text="Select New Starting Time").pack()
    btn2 = Button(top, font=('calibri', 16, 'bold'), text="Exit", command=top.destroy).pack()
    btn3 = Button(top, font=('calibri', 16, 'bold'), text="Save Changes", command=savechanges).pack()
    drop = OptionMenu(top, var, *optionslist) #you need the star up front
    drop.config(font=('calibri', 16, 'bold'))
    drop.pack()
    drop2 = OptionMenu(top, var2, *minutelist)
    drop2.config(font=('calibri', 16, 'bold')) #you need the star up front
    drop2.pack()
    pass

def time():
    present = strftime('%H:%M:%S %p')
    lbl2.config(text = present)

    elapsed_hours = (int(strftime('%H')) - start_hours)
    elapsed_minutes = ((elapsed_hours*60) + int(strftime('%M')) - start_minutes)
    lbl.config(text = "Minutes Passed: " + str(elapsed_minutes) + strftime(':%S'))
    lbl3.config(text = "Minutes Remaining: " + str(1000-elapsed_minutes) + ":" + str(60-int(strftime('%S'))))
    bar['value'] = (elapsed_minutes/10)
    lbl4.config(text = str(bar['value']) + "%")
    lbl2.after(1000, time)


lbl2 = Label(root, font=('calibri', 40, 'bold'))
lbl2.pack(anchor='center')

lbl = Label(root, font=('calibri', 40, 'bold'))
lbl.pack(anchor='center')

lbl3 = Label(root, font=('calibri', 40, 'bold'))
lbl3.pack(anchor='center')

bar = Progressbar(root, length = 400)
#bar['value'] = 20
bar.pack()

lbl4 = Label(root, font=('calibri', 24, 'bold'))
lbl4.pack(anchor='center')

lbl5 = Label(root, font=('calibri', 24, 'bold'))
lbl4.pack(anchor='center')

btn1 = Button(root, font=('calibri', 24, 'bold'), text="Change Set Time", command=changesettime)
btn1.pack(anchor='center')

time()
root.mainloop()