from tkinter import *
root = Tk()
root.title("Blinking Text")
root.geometry("1000x400")

label = Label(root,
              width=50, height=10,
              relief='groove', bd=10,
              bg="indigo", fg="gold", font=("Courier", 20))
label.pack()

def update():
    current = label.cget("text")
    if current == "Hello":
        current = ""
    else:
        current = "Hello"
    label["text"] = current
    root.after(500, update)

update()
