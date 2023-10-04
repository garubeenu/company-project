#=================================
# imports
#=================================
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("PYthon GUI")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1 ,text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2 ,text='Tab 2')



tabControl.pack(expand=1 ,fill="both")


#LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1 ,text=' Mighty Python ')
mighty.grid(row=0 ,column=0 ,padx=8 ,pady=4)

#Label using mighty as the parnt
a_label = ttk.Label(mighty ,text="Enter a name:")
a_label.grid(row=0 ,column=0 ,sticky='W')



#=================================
# Start GUI
#=================================
win.mainloop()
