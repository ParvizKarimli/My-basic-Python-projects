from tkinter import *
root = Tk()


f1 = Frame(root)
f1.pack()

l1 = Label(f1, text="Login:", width=10, anchor=W, fg='#0099ff')
l1.pack(side=LEFT)

e1 = Entry(f1, highlightcolor='#0099ff', highlightthickness=1)
e1.pack()


f2 = Frame(root)
f2.pack()

l2 = Label(f2, text="Password:", width=10, anchor=W, fg='#0099ff')
l2.pack(side=LEFT)

e2 = Entry(f2, show='*', highlightcolor='#0099ff', highlightthickness=1)
e2.pack()


def check():
    lgn = e1.get()
    pss = e2.get()
    if lgn == "mylogin":
        if pss == "mypassword":
            messagebox.showinfo("Welcome Message", ("Welcome " + lgn + "!"))
        else:
            messagebox.showerror("Password Error Message", (lgn+ ", your password is incorrect. Please try again!"))
    else:
        messagebox.showerror("Login Error Message", "No such login found")
            

b = Button(text='Sign In', bg='#0099ff', width=24, fg='white', command=check)
b.pack()
b.config(font=("Helvetica Neue", 10, "bold"))


root.title("Sign In")
