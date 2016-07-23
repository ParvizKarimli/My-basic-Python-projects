from tkinter import *
root = Tk()
root.title("Tracking Coordinates")
root.geometry("650x550-700+10")

def motion(event):
    canvas.delete(ALL)
    pointer = canvas.create_oval(event.x-25, event.y-25,
                                 event.x+25, event.y+25, fill='red')
    current = "x=" + str(event.x) + ", y=" + str(event.y)
    label.config(text=current)
    mycoords.config(text=current)

label = Label(root, width=20, height=5, fg='blue', font="Courier")
label.pack()

tl = Toplevel()
tl.title("Coordinates")
tl.geometry("200x30-450+50")
mycoords = Message(tl)
mycoords.pack()

canvas = Canvas(root, width=500, height=500, bg='cyan')
canvas.bind("<Motion>", motion)
canvas.pack(pady=50)
