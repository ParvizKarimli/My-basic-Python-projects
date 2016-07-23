from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title("Color Chooser")
root.geometry("500x500-500+50")

def colorfunc():
    color = askcolor()
    color_name = color[1]
    root.configure(background=color_name)

button = Button(root, text="Choose Color", command=colorfunc,
                width=30, height=5, bg='indigo', fg='gold')
button.pack()
