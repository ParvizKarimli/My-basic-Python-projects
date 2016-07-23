from tkinter import *
root = Tk()
root.geometry("800x600")

def enter(event):
    canvas.delete(ALL)
    canvas.create_oval(100, 100, 400, 400, fill='red')

def leave(event):
    canvas.delete(ALL)
    canvas.create_rectangle(100, 100, 400, 400, fill='red')

def left(event):
    canvas.delete(ALL)
    canvas.create_polygon(250,50, 450,250, 250,450, 50,250, fill='red')

def right(event):
    canvas.delete(ALL)
    canvas.create_polygon(250,50, 450,250, 50,250, fill='red')

canvas = Canvas(root, width=500, height=500, bg='cyan')
canvas.bind("<Enter>", enter)
canvas.bind("<Leave>", leave)
canvas.bind("<Button-1>", left)
canvas.bind("<Button-3>", right)
canvas.pack()

