#=============================
# imports
#=============================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

win.size()

ttk.Label(win ,text="A Label").grid(column=0 ,row=0)
ttk.Label(win ,text="B Label").grid(column=1 ,row=1)


#=============================
# Start GUI
#=============================
win.mainloop()
