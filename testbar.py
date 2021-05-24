import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
canv = tk.Tk()
canv.title("Tkinter Progressbar")
canv.geometry('250x100')
bar = Progressbar(canv, length=240, style='grey.Horizontal.TProgressbar')
bar['value'] = 1
bar.grid(column=0, row=0)
canv.mainloop()