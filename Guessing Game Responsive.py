from tkinter import *
root = Tk()
root.title("Guessing Game")
root.geometry("1000x500")
import random

var = "Choose a number in range [1, 10]"
txtvar = StringVar()
txtvar.set(var)

def check():
    number = random.choice(range(1, 11))
    try:
        if int(entry.get()) == number:
            var = "You WON! \n" + "Entered Number: " + str(entry.get()) + "; " + "Random Number: " + str(number) + "\n Play again!"
            txtvar.set(var)
        else:
            var = "You LOST! \n" + "Entered Number: " + str(entry.get()) + "; " + "Random Number: " + str(number) + "\n Try again!"
            txtvar.set(var)
    except:
        pass
    #root.after(1000, check)

def clear(event):
    entry.delete(0, END)

def valfunc(value):
    if not value:
        None
        return True
    try:
        int(value)
    except:
        return False
    if 1 <= int(value) <= 10:
        return True
    return False

    
label = Label(root, textvariable=txtvar,
              relief='groove', width=60, height=10,
              bg='indigo', fg='gold', font='Courier')
label.pack()

vcmd = root.register(valfunc)
entry = Entry(root, bg='indigo', fg='gold',
              font=('Courier', 50), width=2,
              validate='all', validatecommand=(vcmd, "%P"))
entry.bind("<Button-1>", clear)
entry.pack()

button = Button(root, text="Check", command=check,
                width=75, height=2, cursor='hand2',
                bg='indigo', fg='gold', font=('Courier', 20))
button.pack()
