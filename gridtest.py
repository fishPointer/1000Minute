from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Death Clock")
root.geometry("800x800")

global i
i = 0
global MYAGE
MYAGE = 500

for r in range(32):
   for c in range(32):
        Label(root, text='[ ]', borderwidth=1 ).grid(row=r,column=c)

for r in range(32):
    for c in range(32):
        checkstr = "[x]"
        if i < MYAGE:
            Label(root, text=checkstr, borderwidth=1).grid(row=r, column=c)
        i += 1


root.mainloop()