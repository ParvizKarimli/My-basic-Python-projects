from tkinter import *
root = Tk()
import random

f = Frame(root, )
f.pack()

lf = Label(f, text="Hello world!",
           cursor='heart', font="Impact",
           bg="cyan", fg="red",
           bd=10, relief="groove",
           width=73,
           )
lf.pack(side=TOP)

quotlist = [
"""
1)“Talk is cheap. Show me the code.” 
― Linus Torvalds
""",

"""
2)“When you don't create things, you become defined by your tastes rather than ability. your tastes only narrow & exclude people. so create.” 
― Why The Lucky Stiff
""",

"""
3)“I'm not a great programmer; I'm just a good programmer with great habits.”
― Kent Beck
""",

"""
4)“A language that doesn't affect the way you think about programming is not worth knowing.” 
― Alan J. Perlis
""",

"""
5)“The most disastrous thing that you can ever learn is your first programming language.” 
― Alan Kay
""",
]

quotlist2 = []

i = 0

def f():
    try:
        global i
        tl = Toplevel()
        txtvar = StringVar()
        txtvar.set(quotlist[i])
        l = Label(tl, textvariable=txtvar,
                  bg="indigo", fg="red",font=("Script", 20))
        l.pack()
        tl.title("Quote NO %s" %(i+1))
        i += 1
    except:
        i = 0
        
b = Button(root, text="Click to get a quote sequentally from the quote list", command=f,
           font="Courier", cursor='hand1', width=59, bd=5, bg='violet', fg='yellow')
b.pack()


def f2():
    tl = Toplevel()
    rq = random.choice(quotlist)
    txtvar = StringVar()
    txtvar.set(rq)
    l = Label(tl, textvariable=txtvar,
              bg="orange", fg="turquoise", font=("Comic Sans MS", 15))
    l.pack()
    tl.title("Random Quote NO %s"%(i+1))
    
b2 = Button(root, text="Click to get a random programming quote from the quote list", command=f2,
           cursor="hand2", bg="purple", fg="gold", font="Courier")
b2.pack()

root.title("Click")
