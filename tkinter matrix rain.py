import random
from tkinter import *
root = Tk()
root.title("Matrix Rain")
root.geometry("500x350")

text = Label(root, bg="black", fg="green", font="Terminal",
            width=100, height=30)
text.pack()

def update():
    text.config(text=
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n" +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                chr(random.choice(range(0x30a1, 0x30ff + 1))) +
                "\n"
                )
    root.after(1, update)

update()