from tkinter import *
root = Tk()

def f1():
    last = cb1
    if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
        last.deselect()
        messagebox.showerror("Error Message", "Cannot select all!")

var1 = IntVar()
var1.set(0)
cb1 = Checkbutton(root, variable=var1, command=f1)
cb1.pack()

def f2():
    last = cb2
    if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
        last.deselect()
        messagebox.showerror("Error Message", "Cannot select all!")

var2 = IntVar()
var2.set(0)
cb2 = Checkbutton(root, variable=var2, command=f2)
cb2.pack()

def f3():
    last = cb3
    if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
        last.deselect()
        messagebox.showerror("Error Message", "Cannot select all!")

var3 = IntVar()
var3.set(0)
cb3 = Checkbutton(root, variable=var3, command=f3)
cb3.pack()
