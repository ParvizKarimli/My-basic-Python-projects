from tkinter import *
root = Tk()
import time


label_local = Label(root, text="Local Time:",
                    bg="indigo", fg="gold", font="Courier",
                    width=20, height=5,
                    relief='groove', bd=5)
label_local.grid(row=0, column=0)

label_ny = Label(root, text="New York:",
                 bg="indigo", fg="gold", font="Courier",
                 width=20, height=5,
                 relief='groove', bd=5)
label_ny.grid(row=1, column=0)

label_local_2 = Label(root,
                    bg="gold", fg="indigo", font="Courier",
                    width=25, height=5,
                    relief='groove', bd=5)
label_local_2.grid(row=0, column=1)

label_ny_2 = Label(root,
                 bg="gold", fg="indigo", font="Courier",
                 width=25, height=5,
                 relief='groove', bd=5)
label_ny_2.grid(row=1, column=1)


def update():

    label_local_2.config(text=(time.strftime("%x %X ")))
    
    label_ny_2.config(text=(
        str(time.gmtime().tm_hour - 3)) + ":" +
        str(time.localtime().tm_min) + ":" +
        str(time.localtime().tm_sec)
                      )

    root.after(1, update)


update()
