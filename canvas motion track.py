from tkinter import *
root = Tk()
root.title("Motion Track")
root.geometry("800x600")

def motion(event):
    oval = canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill='red')

canvas = Canvas(root, width=500, height=500, bg='cyan')
canvas.bind("<Motion>", motion)
canvas.pack(pady=50)
