from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.resizable(False, False)

def time():
    string = strftime("%d-%m-%Y %H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=("Arial", 75, 'bold'), foreground="white", background="black")
lbl.pack(anchor="center")

time()

root.mainloop()
