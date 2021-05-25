"""
Ian Tralmer/fishPointer
May 25, 2021
1000 Minute Clock
"Every day you have just 1000 minutes to make things happen"
Counts down 1000 Minutes from a set Wakeup Time. Default is 5:00am
"""

# Uses Tkinter for GUI, PIL for Program Icon, strftime for time, and tkinter.tkk for a Progress Bar
from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter.ttk import Progressbar

# Build window
root = Tk()
root.title("1000 Minutes")
root.geometry("700x300")
img = PhotoImage(file='/home/eein/Documents/Lab/Code/1000Minute/skull.png')
root.call('wm', 'iconphoto', root._w, img)

# Define Set Wakeup Time
global start_hours
global start_minutes
start_hours = 5
start_minutes = 0

# Tkinter Variables that pass value to the Wakeup Globals
var_hours = IntVar()
var_minutes = IntVar()
var_hours.set(5)
var_minutes.set(00)

# Dropdown list options
hoursList = [1,2,3,4,5,6,7,8,9,10,11,12]
minuteList = [00,10,20,30,40,50]

# Saves Changes made in the menu
def savechanges():
    global start_hours
    global start_minutes
    start_hours = var_hours.get()
    start_minutes = var_minutes.get()

# Opens the Menu
def changesettime():
    # Build new menu window
    top = Toplevel()
    top.title("Select New Starting Time")
    top.geometry("300x300")
    img = PhotoImage(file='/home/eein/Documents/Lab/Code/1000Minute/skull.png')
    root.call('wm', 'iconphoto', top._w, img)

    # Defining Labels, Dropdowns, and Buttons
    lbl_select = Label(top, font=('calibri', 16, 'bold'), text="Select New Starting Time")
    drop_hours = OptionMenu(top, var_hours, *hoursList)
    drop_minutes = OptionMenu(top, var_minutes, *minuteList)
    drop_hours.config(font=('calibri', 16, 'bold'))
    drop_minutes.config(font=('calibri', 16, 'bold'))
    btn_save = Button(top, font=('calibri', 16, 'bold'), text="Save Changes", command=savechanges)
    btn_exit = Button(top, font=('calibri', 16, 'bold'), text="Exit Menu", command=top.destroy)

    # Render
    lbl_select.pack()
    drop_hours.pack()
    drop_minutes.pack()
    btn_save.pack()
    btn_exit.pack()

# Updates the current time, minutes passed, minutes remaining, and progress bar each second
def time():
    # Set time to present
    present = strftime('%H:%M:%S %p')
    lbl_current_time.config(text = present)

    # Calculate elapsed/remaining
    elapsed_hours = (int(strftime('%H')) - start_hours)
    elapsed_minutes = ((elapsed_hours*60) + int(strftime('%M')) - start_minutes)

    # Print Updates
    lbl_minutes_passed.config(text = "Minutes Passed: " + str(elapsed_minutes) + strftime(':%S'))
    lbl_minutes_remaining.config(text = "Minutes Remaining: " + str(1000-elapsed_minutes) + ":" + str(60-int(strftime('%S'))))
    bar['value'] = (elapsed_minutes/10)
    lbl_ratio.config(text = str(bar['value']) + "%")

    # Wait 1 second, then repeat this entire function
    lbl_current_time.after(1000, time)

# Defining Labels/Progress Bar/Menu Button
lbl_current_time = Label(root, font=('calibri', 40, 'bold'))
lbl_minutes_passed = Label(root, font=('calibri', 40, 'bold'))
lbl_minutes_remaining = Label(root, font=('calibri', 40, 'bold'))
bar = Progressbar(root, length = 400)
lbl_ratio = Label(root, font=('calibri', 24, 'bold'))
btn_starting = Button(root, font=('calibri', 24, 'bold'), text="Change Set Time", command=changesettime)

# Render
lbl_current_time.pack()
lbl_minutes_passed.pack()
lbl_minutes_remaining.pack()
bar.pack()
lbl_ratio.pack()
btn_starting.pack()

# Call time once on startup, time loops itself afterwards. mainloop for window
time()
root.mainloop()