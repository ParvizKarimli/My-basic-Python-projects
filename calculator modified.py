from tkinter import *
root = Tk()
root.title("Calculator")

firstnumbox = Text(root, width=25, height=2, bd=5, relief="groove")
firstnumbox.pack()

opbox = Text(root, width=5, height=2, bd=5, relief="groove")
opbox.pack()

secondnumbox = Text(root, width=25, height=2, bd=5, relief="groove")
secondnumbox.pack()

resultbox = Text(root, width=0, height=0)
resultbox.pack()

fr = Frame(root)
fr.pack()

def onefunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "1")
    else:
        secondnumbox.insert(END, "1")

one = Button(fr, text="1", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=onefunc)
one.grid(row=2, column=0)

def twofunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "2")
    else:
        secondnumbox.insert(END, "2")

two = Button(fr, text="2", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=twofunc)
two.grid(row=2, column=1)

def threefunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "3")
    else:
        secondnumbox.insert(END, "3")

three = Button(fr, text="3", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=threefunc)
three.grid(row=2, column=2)

def fourfunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "4")
    else:
        secondnumbox.insert(END, "4")

four = Button(fr, text="4", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=fourfunc)
four.grid(row=1, column=0)

def fivefunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "5")
    else:
        secondnumbox.insert(END, "5")

five = Button(fr, text="5", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=fivefunc)
five.grid(row=1, column=1)

def sixfunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "6")
    else:
        secondnumbox.insert(END, "6")

six = Button(fr, text="6", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=sixfunc)
six.grid(row=1, column=2)

def sevenfunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "7")
    else:
        secondnumbox.insert(END, "7")

seven = Button(fr, text="7", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=sevenfunc)
seven.grid(row=0, column=0)

def eightfunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "8")
    else:
        secondnumbox.insert(END, "8")

eight = Button(fr, text="8", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=eightfunc)
eight.grid(row=0, column=1)

def ninefunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "9")
    else:
        secondnumbox.insert(END, "9")

nine = Button(fr, text="9", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=ninefunc)
nine.grid(row=0, column=2)

def zerofunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, "0")
    else:
        secondnumbox.insert(END, "0")

zero = Button(fr, text="0", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=zerofunc)
zero.grid(row=3, column=1)

def dotfunc():
    if len(opbox.get(1.0, "end-1c")) == 0:
        firstnumbox.insert(END, ".")
    else:
        secondnumbox.insert(END, ".")

dot = Button(fr, text=".", width=25, height=2, cursor="hand2", bd=5, relief="raised",
             command=dotfunc)
dot.grid(row=6, column=1)

def plusfunc():
    opbox.insert(END, "+")

plus = Button(fr, text="+", width=25, height=2, cursor="hand2", bd=5, relief="raised",
              command=plusfunc)
plus.grid(row=4, column=0)

def minusfunc():
    opbox.insert(END, "-")

minus = Button(fr, text="-", width=25, height=2, cursor="hand2", bd=5, relief="raised",
               command=minusfunc)
minus.grid(row=4, column=2)

def timesfunc():
    opbox.insert(END, "*")

times = Button(fr, text="*", width=25, height=2, cursor="hand2", bd=5, relief="raised",
               command=timesfunc)
times.grid(row=5, column=0)

def dividefunc():
    opbox.insert(END, "/")

divide = Button(fr, text="/", width=25, height=2, cursor="hand2", bd=5, relief="raised",
               command=dividefunc)
divide.grid(row=5, column=2)

def equalfunc():
    try:
        if opbox.get(1.0, "end-1c") == "+":
            resultbox.insert(END, (float(firstnumbox.get(1.0, "end-1c")) + float(secondnumbox.get(1.0, "end-1c"))))
            firstnumbox.delete(0.0, END)
            opbox.delete(0.0, END)
            secondnumbox.delete(0.0, END)
            firstnumbox.insert(END, resultbox.get(1.0, "end-1c"))
            resultbox.delete(0.0, END)
        elif opbox.get(1.0, "end-1c") == "-":
            resultbox.insert(END, (float(firstnumbox.get(1.0, "end-1c")) - float(secondnumbox.get(1.0, "end-1c"))))
            firstnumbox.delete(0.0, END)
            opbox.delete(0.0, END)
            secondnumbox.delete(0.0, END)
            firstnumbox.insert(END, resultbox.get(1.0, "end-1c"))
            resultbox.delete(0.0, END)
        elif opbox.get(1.0, "end-1c") == "*":
            resultbox.insert(END, (float(firstnumbox.get(1.0, "end-1c")) * float(secondnumbox.get(1.0, "end-1c"))))
            firstnumbox.delete(0.0, END)
            opbox.delete(0.0, END)
            secondnumbox.delete(0.0, END)
            firstnumbox.insert(END, resultbox.get(1.0, "end-1c"))
            resultbox.delete(0.0, END)
        elif opbox.get(1.0, "end-1c") == "/":
            resultbox.insert(END, (float(firstnumbox.get(1.0, "end-1c")) / float(secondnumbox.get(1.0, "end-1c"))))
            firstnumbox.delete(0.0, END)
            opbox.delete(0.0, END)
            secondnumbox.delete(0.0, END)
            firstnumbox.insert(END, resultbox.get(1.0, "end-1c"))
            resultbox.delete(0.0, END)
        else:
            print("No such operation!")
    except:
        pass

equal = Button(fr, text="=", width=25, height=2, cursor="hand2", bd=5, relief="raised",
               command=equalfunc)
equal.grid(row=6, column=0)

def clearfunc():
    firstnumbox.delete(0.0, END)
    opbox.delete(0.0, END)
    secondnumbox.delete(0.0, END)
    resultbox.delete(0.0, END)
    

clear = Button(fr, text="C", width=25, height=2, cursor="hand2", bd=5, relief="raised",
               command=clearfunc)
clear.grid(row=6, column=2)
