from tkinter import *
root = Tk()
root.title("Notebook")

sby = Scrollbar(root, orient='vertical', cursor='hand1')
sby.pack(fill='y', side='right')

t = Text(root, cursor='bottom_tee', bg='cyan', fg='red',
         bd=10, relief='groove',
         height=10, width=50,
         padx=30, pady=30,
         selectbackground='yellow', selectforeground='green',
         selectborderwidth=5, highlightthickness=10,
         highlightbackground='violet', highlightcolor='purple',
         insertwidth=2, insertborderwidth=10,
         insertontime=200, insertofftime=100, insertbackground='blue',
         state='normal', spacing1=5,
         spacing2=5, spacing3=5,
         yscrollcommand=sby.set, font=("Courier", 20), wrap='word')
t.pack()

sby.config(command=t.yview)


frame = Frame(root)
frame.pack()

def f():
    fob = open("notesave.txt", 'w')
    fob.write(t.get(1.0, "end-1c"))
    fob.close()

b = Button(frame, text="Save", command=f,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
b.pack(side=LEFT)


def f2():
    fob = open("C:/Users/MIRI/AppData/Local/Programs/Python/Python35-32/notesave.txt", 'r')
    tl = Toplevel(cursor='spider')
    tl.title("Saved Text")
    sby = Scrollbar(tl, orient='vertical', cursor='hand1')
    sby.pack(fill='y', side='right')
    t = Text(tl, cursor='bottom_tee', bg='cyan', fg='red',
         bd=10, relief='groove',
         height=10, width=50,
         padx=30, pady=30,
         selectbackground='yellow', selectforeground='green',
         selectborderwidth=5, highlightthickness=10,
         highlightbackground='violet', highlightcolor='purple',
         insertwidth=2, insertborderwidth=10,
         insertontime=200, insertofftime=100, insertbackground='blue',
         state='normal', spacing1=5,
         spacing2=5, spacing3=5,
         yscrollcommand=sby.set, font=("Courier", 20), wrap='word')
    t.pack()
    t.insert(INSERT, fob.read())
    sby.config(command=t.yview)

    #PERIOD
    frame = Frame(tl)
    frame.pack()
    def f():
        fob = open("C:/Users/MIRI/AppData/Local/Programs/Python/Python35-32/notesave.txt", 'w')
        fob.write(t.get(1.0, "end-1c"))
        fob.close()
    b = Button(frame, text="Save", command=f,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
    b.pack(side=LEFT)
    b2 = Button(frame, text="Open", command=f2,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
    b2.pack(side=LEFT)
    def f3():
        tl.destroy()
    b3 = Button(frame, text="Quit", command=f3,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
    b3.pack(side=RIGHT)
    
    
b2 = Button(frame, text="Open", command=f2,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
b2.pack(side=LEFT)


def f3():
    root.destroy()
    
b3 = Button(frame, text="Quit", command=f3,
           font='Impact', fg='gold', bg='indigo',
           width=20, cursor='hand2', bd=5, relief='ridge',
           activebackground='orange', activeforeground='blue')
b3.pack(side=RIGHT)
