from tkinter import *
root = Tk()
root.title("Motion Track")
root.geometry("800x600")

def motion(event):
    oval = canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill='red')
    def update():
        current = canvas.itemcget(oval, "fill")
        if current == 'red':
            current = 'green'
        elif current == 'green':
            current = 'blue'
        else:
            current = 'red'
        canvas.itemconfig(oval, fill=current)
        root.after(500, update)
    update()

canvas = Canvas(root, width=500, height=500, bg='cyan')
canvas.bind("<Motion>", motion)
canvas.pack(pady=50)
