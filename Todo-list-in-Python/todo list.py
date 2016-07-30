from tkinter import *
root = Tk()
root.title("Todo List")

fr = Frame(root)
fr.pack()

l = Label(fr, text="New Task:", fg="blue", font='Courier', height=5)
l.pack(side=LEFT)

e = Entry(fr, width=100, fg='red', highlightthickness=1,
          highlightcolor='purple', highlightbackground='violet', font='Courier')
e.pack(side=LEFT)

def addfunc():
    if len(e.get()) == 0:
        messagebox.showerror("Error Message", "Please don't add empty line!")
    else:
        lb1.insert(END, e.get())

b = Button(fr, text="Add", command=addfunc, cursor='hand2',
           fg="gold", bg="indigo",
           activeforeground='orange', activebackground='cyan',
           bd=2, relief='groove', font='Courier')
b.pack(side=RIGHT)

lfr1 = LabelFrame(root, text="Tasks", fg='#0099ff', font='Courier')
lfr1.pack()

sbar1 = Scrollbar(lfr1, orient='vertical', cursor='hand1')
sbar1.pack(fill='y', side='right')

lb1 = Listbox(lfr1, cursor='hand2', width=100, height=10, fg='lime', highlightthickness=1,
              highlightcolor='purple', highlightbackground='violet',
              selectforeground='#0099ff', selectbackground='lightgreen',
              yscrollcommand=sbar1.set, font='Courier', selectmode='browse')
lb1.pack()

sbar1.config(command=lb1.yview)

def donefunc():
    try:
        lb2.insert(END, lb1.get(lb1.curselection()))
        lb1.delete(lb1.curselection())
    except:
        pass

b2 = Button(lfr1, text="Done", command=donefunc, cursor='hand2',
            fg="gold", bg="indigo",
            activeforeground='orange', activebackground='cyan',
            bd=2, relief='groove', font='Courier')
b2.pack(side=LEFT)

def removefunc():
    try:
        lb1.delete(lb1.curselection())
    except:
        pass

b21 = Button(lfr1, text="Remove", command=removefunc, cursor='hand2',
             fg="gold", bg="indigo",
             activeforeground='orange', activebackground='cyan',
             bd=2, relief='groove', font='Courier')
b21.pack(side=RIGHT)

lfr2 = LabelFrame(root, text="Completed", fg='#0099ff', font='Courier')
lfr2.pack()

sbar2 = Scrollbar(lfr2, orient='vertical', cursor='hand1')
sbar2.pack(fill='y', side='right')

lb2 = Listbox(lfr2, cursor='hand2', width=100, height=10, fg='green', highlightthickness=1,
              highlightcolor='purple', highlightbackground='violet',
              selectforeground='#0099ff', selectbackground='lightgreen',
              yscrollcommand=sbar2.set, font='Courier', selectmode='browse')
lb2.pack()

sbar2.config(command=lb2.yview)

def undonefunc():
    try:
        lb1.insert(END, lb2.get(lb2.curselection()))
        lb2.delete(lb2.curselection())
    except:
        pass

b3 = Button(lfr2, text="Undone", command=undonefunc, cursor='hand2',
            fg="gold", bg="indigo",
            activeforeground='orange', activebackground='cyan',
            bd=2, relief='groove', font='Courier')
b3.pack(side=LEFT)

def deletefunc():
    try:
        lb2.delete(lb2.curselection())
    except:
        pass

b31 = Button(lfr2, text="Delete", command=deletefunc, cursor='hand2',
             fg="gold", bg="indigo",
             activeforeground='orange', activebackground='cyan',
             bd=2, relief='groove', font='Courier')
b31.pack(side=RIGHT)

def savefunc():
    fob = open("tasksave.txt", 'w')
    fob.write(str(lb1.get(0, END)) + "\n" + str(lb2.get(0, END)))

def quitfunc():
    result = messagebox.askquestion("Save?", "Do you wish to save before you quit?")
    if result == 'yes':
        fob = open("tasksave.txt", 'w')
        fob.write(str(lb1.get(0, END)) + "\n" + str(lb2.get(0, END)))
        root.destroy()
    else:
        root.destroy()
        
menubar = Menu(root, cursor='hand2')
filemenu = Menu(menubar)
filemenu.add_command(label="Save", command=savefunc)
filemenu.add_command(label="Quit", command=quitfunc)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
