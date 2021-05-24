from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from time import strftime
from tkinter.ttk import Progressbar

global start_hours
global start_minutes
start_hours = 5
start_minutes = 0

root = Tk()
root.title("1000 Minutes")
root.geometry("700x300")
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)


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
bar['value'] = 20
bar.pack()

lbl4 = Label(root, font=('calibri', 24, 'bold'))
lbl4.pack(anchor='center')


time()
root.mainloop()