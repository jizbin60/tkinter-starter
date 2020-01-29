# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="goodbye")

# Place the label in the window at 0, 0
lbl.grid(column=3, row=3)

btn = Button(window, text="Click Me")
 
btn.grid(column=5, row=6)

lbl.grid(column=3, row=3)

btn = Button(window, text="Click Me")
 
btn.grid(column=5, row=5)

firstLabel = Label(window, text="Hello", font=("Arial Bold", 50))
firstLabel.grid(column=1, row=1) 

secondLabel = Label(window, text = "This is a label") # Create the label
secondLabel.grid(column=2, row=2) 

breakfast = Label(window, text="WOWWWW")
breakfast.grid(column = 4, row = 4)

chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)

menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)

from tkinter.ttk import Progressbar
 
 
from tkinter import ttk

style = ttk.Style()
 
style.theme_use('default')
 
style.configure("black.Horizontal.TProgressbar", background='black')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 70
 
bar.grid(column=0, row=0)

window.mainloop()     # Keep the window open
