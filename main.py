from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("clock")
def time():
    string = strftime ('%H:%M:%S:%r')
    Label.config(text = string)
    Label.after(1000,time)
    label = Label(root,font = ("ds-digital",80),background = "black",foreground = "cyan")
    Label.pack(anchor='center')
    time()
    mainloop()
