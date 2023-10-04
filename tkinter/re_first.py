#===================
# imports
#===================
import tkinter as tk
import time
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

#========================================================================================================================
class ToolTip(object):
    def __init__(self ,widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self ,tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x ,y ,_cx ,cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
#        tw.wm_overrideredirect(False)
        tw.wm_geometry("+%d+%d" % (x ,y))

        label = tk.Label(tw ,text=tip_text ,justify=tk.LEFT ,background="#ffffe0" ,relief=tk.SOLID ,borderwidth=1,font=("tahama" ,"8" ,"normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()
#========================================================================================================================
def create_ToolTip(widget ,text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>' ,enter)
    widget.bind('<Leave>' ,leave)


# Button Click Event Function
def click_me():
    action.configure(text="Hello " + name.get() + '   ' + number.get())

# Display a Message Box
def _msgBox():
#    msg.showinfo('Python Message Info Box' , 'A Python GUI created using tkinter: \nThe year is 2017.')
#    msg.showwarning('Python Message Warning Box' , 'A Python GUI created using tkinter:'
#                    '\nWarning: There might be a bug in this code.')
#    msg.showerror('Python Message Error Box' ,'A Python GUI created using tkiner:'
#                  '\nError: Houston ~ we DO have a serious PROBLEM!')
    answer = msg.askyesnocancel("Python Message Multi Choice Box","Are you sure you really wish to do this?")
    print(answer)

# 스핀 박스 콜백
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT ,value + '\n')


# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1 ,text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2 ,text='Tab 2')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3 ,text='Tab 3')


tabControl.pack(expand=1 ,fill="both")

# Tab Control 3 -------------------------------------------
tab3_frame = tk.Frame(tab3 ,bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame ,width=150 ,height=80 ,highlightthickness=0 ,bg='orange')
    canvas.grid(row=orange_color ,column=orange_color)



# We are creating acontainer fram to hold all other widgets
mighty = ttk.LabelFrame(tab1 ,text=' Mighty Python ')
mighty.grid(row=0 ,column=0 ,padx=8 ,pady=4)

# We are creating acontainer fram to hold all other widgets
mighty2 = ttk.LabelFrame(tab2 ,text=' The Snake ')
mighty2.grid(row=0 ,column=0 ,padx=8 ,pady=4)



# Changing our Label
ttk.Label(mighty ,text="your name? : ").grid(row=0 ,column=0 ,sticky='W')

# Add a Entry
name = tk.StringVar()
name_entered = ttk.Entry(mighty ,width=12 ,textvariable=name)
name_entered.grid(row=1 ,column=0)

# Add a Label
ttk.Label(mighty ,text="Choose a number : ").grid(row=0 ,column=1)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty ,width=12 ,textvariable=number ,state='readonly')
number_chosen['values'] = (1 ,2 ,4 ,42 ,100)
number_chosen.grid(row=1 ,column=1)
number_chosen.current(0)

# Add a Button
action = ttk.Button(mighty ,text="Click me!" ,command=click_me)
action.grid(row=1 ,column=2)
create_ToolTip(action ,'This is a Button')

# 위젯 추가하기
spin = tk.Spinbox(mighty ,values=(1,2,4,42,100) ,width=20 ,bd=8 ,command=_spin)
spin.grid(row=2,column=0)

create_ToolTip(spin ,'This is a Spin control')

# spin = Spinbox(mighty ,values=(1,2,4,42,100) ,width=50 ,bd=8 ,command=_spin)
# spin.grid(row=2,column=1)


# Using a scrolled Text control
scrol_w = 50
scrol_h =  3
scr = scrolledtext.ScrolledText(mighty ,width=scrol_w ,height=scrol_h ,wrap=tk.WORD)
scr.grid(row=3 ,column=0 ,columnspan=3 )




chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2 ,text="Disabled" ,variable=chVarDis ,state='disabled')
check1.select()
check1.grid(row=4 ,column=0 ,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2 ,text="Unchecked" ,variable=chVarUn)
check2.deselect()
check2.grid(row=4 ,column=1 ,sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2 ,text="Disabled" ,variable=chVarEn)
check3.select()
check3.grid(row=4 ,column=2 ,sticky=tk.W)




# Radiobutton Globals
colors = ["Blue" ,"Gold" ,"Red"]

# Radiobutton Callback
def radCall():
    win.configure(background=colors[radVar.get()])

# create three Radiobuttons using one variable
radVar = tk.IntVar()

radVar.set(3)

for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col] ,variable=radVar ,value=col ,command=radCall)
    curRad.grid(row=6 ,column=col ,sticky=tk.W)





# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty2 ,text= ' ProgressBar ')
buttons_frame.grid(row=7 ,column=0 ,padx=20 ,pady=40)
# buttons_frame.grid(row=7 ,column=1)

def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        time.sleep(0.1)
        progress_bar["value"] = i
        progress_bar.update()
    progress_bar["value"] = 0

def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)

# Place labels into the container element
ttk.Button(buttons_frame ,text="Run Progressbar    " ,command=run_progressbar).grid(row=0 ,column=0 ,sticky=tk.W)
ttk.Button(buttons_frame ,text="Start Progressbar  " ,command=start_progressbar).grid(row=1 ,column=0 ,sticky=tk.W)
ttk.Button(buttons_frame ,text="Stop immediately   " ,command=stop_progressbar).grid(row=2 ,column=0 ,sticky=tk.W)
ttk.Button(buttons_frame ,text="Stop after second  " ,command=progressbar_stop_after).grid(row=3 ,column=0 ,sticky=tk.W)

progress_bar = ttk.Progressbar(tab2 ,orient='horizontal' ,length=286 ,mode='determinate')
progress_bar.grid(column=0,pady=2)


                 


for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8 ,pady=4)

for child in mighty.winfo_children():
    child.grid_configure(sticky='W')

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create menu and add menu items
file_menu = Menu(menu_bar ,tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit" ,command=_quit)
menu_bar.add_cascade(label="File" ,menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar ,tearoff=0)
menu_bar.add_cascade(label="help" ,menu=help_menu)
help_menu.add_command(label="About" ,command=_msgBox)



name_entered.focus()

#===================
# start
#===================
win.mainloop()
