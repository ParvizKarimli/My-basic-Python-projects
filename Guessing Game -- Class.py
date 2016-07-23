from tkinter import *
import random

class Guess:
    def __init__(self, master):
        self.master = master

        self.txtvar = StringVar()
        self.txtvar.set("Enter a number in range [1, 10]")
        self.label = Label(master, textvariable=self.txtvar, cursor='heart', 
                           relief='groove', bd=5, bg='indigo', fg='gold',
                           font=("Courier", 20), width=50, height=10)
        self.label.pack()

        vcmd = master.register(self.valfunc)
        self.entry = Entry(master, relief='groove', bd=5,
                           bg='indigo', fg='gold', font=("Courier", 50), width=2,
                           validate='key', validatecommand=(vcmd, '%P'))
        self.entry.bind("<Button-1>", self.clear)
        self.entry.pack()

        self.button = Button(master, text="Check", command=self.check, cursor='hand2',
                             relief='groove', bd=5, bg='indigo', fg='gold',
                             font=("Courier", 20), width=50)
        self.button.pack()

    def check(self):
        try:
            number = random.choice(range(1, 11))
            if int (self.entry.get()) == number:
                var = "Congrats! You WON! \n" + "Your number: " + str(self.entry.get()) + "; " "Random number: " + str(number) + "\n You can play again!"
                self.txtvar.set(var)
            else:
                var = "Sorry! You LOST... \n" + "Your number: " + str(self.entry.get()) + "; " "Random number: " + str(number) + "\n Try again!"
                self.txtvar.set(var)
            self.entry.delete(0, END)
        except:
            pass
        #root.after(1000, self.check) #automate
                                    #so you only need to enter a number and press the check button for only once

    def valfunc(self, value):
        if not value:
            None
            return True
        try:
            int(value)
            if 1 <= int(value) <= 10:
                return True
            return False
        except:
            return False

    def clear(self, event):
        self.entry.delete(0, END)

root = Tk()
root.title("Guess The Number")
root.geometry("1000x500")

obj = Guess(root)
