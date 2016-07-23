from tkinter import *
root = Tk()
root.title("Guessing Game")
root.geometry("600x300")
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
    #root.after(2000, check)



    
label = Label(root, textvariable=txtvar,
              relief='groove', width=60, height=10,
              bg='indigo', fg='gold', font='Courier')
label.pack()

entry = Scale(root, bg='indigo', fg='gold', font='Terminal',
                from_=1, to=10, orient='horizontal', width=50, length=600, cursor='hand1')
entry.pack()

button = Button(root, text="Check", command=check,
                width=75, height=2, cursor='hand2',
                bg='indigo', fg='gold', font='Impact')
button.pack()
