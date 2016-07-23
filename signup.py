from tkinter import *
root = Tk()


Label(root).pack() #empty space line


#First name

ffname = Frame(root)
ffname.pack()

lfname = Label(ffname, text="First Name:", width=10, anchor=CENTER)
lfname.pack(side=LEFT)

efname = Entry(ffname, width=50)
efname.pack()


Label(root).pack() #empty space line


#Last name

flname = Frame(root)
flname.pack()

llname = Label(flname, text="Last Name:", width=10, anchor=CENTER)
llname.pack(side=LEFT)

elname = Entry(flname, width=50)
elname.pack()


Label(root).pack() #empty space line


#Birthday

fbday = Frame(root)
fbday.pack()

lbday = Label(fbday, text="Birthday:", width=20, anchor=W)
lbday.pack(side=LEFT)

#Day

lday = Label(fbday, text="Day")
lday.pack()

dayvalues = ["Day"]
for d in range(1, 32):
    dayvalues.append(str(d))

sboxday = Spinbox(fbday, values=dayvalues)
sboxday.pack()

#Month

lmonth = Label(fbday, text="Month")
lmonth.pack()

monthvalues = ['Month', 'January','February','March','April','May','June','July','August','September','October','November', 'December']
sboxmonth = Spinbox(fbday, values=monthvalues)
sboxmonth.pack()

thirtyone = ['January','March','May','July','August','October', 'December']
thirty = ['April','June','September','November']
twentynine = ['February']

#Year

lyear = Label(fbday, text="Year")
lyear.pack()

yearvalues = ["Year"]
for y in range(1900, 2016):
    yearvalues.append(str(y))

sboxyear = Spinbox(fbday, values=yearvalues)
sboxyear.pack()


Label(root).pack() #empty space line


#Gender

fgender = Frame(root)
fgender.pack()

lgender = Label(fgender, text="Gender:", width=20, anchor=W)
lgender.grid(row=0, column=0)

gendervar = StringVar()
gendervar.set(' ')

#Male

rbmale = Radiobutton(fgender, text="Male", variable=gendervar, value="Male")
rbmale.grid(row=0, column=1)

#Female

rbfemale = Radiobutton(fgender, text="Female", variable=gendervar, value="Female")
rbfemale.grid(row=0, column=2)


Label(root).pack() #empty space line


#Email

femail = Frame(root)
femail.pack()

lemail = Label(femail, text="Email:", padx=29)
lemail.pack(side=LEFT)

eemail = Entry(femail, width=50)
eemail.pack()


Label(root).pack() #empty space line


#Password

fpwd = Frame(root)
fpwd.pack()

lpwd = Label(fpwd, text="Password:", padx=20)
lpwd.pack(side=LEFT)

epwd = Entry(fpwd, show='*', width=50)
epwd.pack()


Label(root).pack() #empty space line


#Retype Password

frpwd = Frame(root)
frpwd.pack()

lrpwd = Label(frpwd, text="Retype Password:")
lrpwd.pack(side=LEFT)

erpwd = Entry(frpwd, show='*', width=50)
erpwd.pack()


Label(root).pack() #empty space line


#Sign Up

fbutton = Frame(root)
fbutton.pack()

def signup():

    #First Name
    if len(efname.get()) == 0:
        messagebox.showerror("Error Message", "Please type your first name!")
        
    #Last Name
    elif len(elname.get()) == 0:
        messagebox.showerror("Error Message", "Please type your last name!")

        
    #Birth Day
    elif len(sboxday.get()) == 0:
        messagebox.showerror("Error Message", "Please don't leave your birth day empty!")
    elif sboxday.get() not in dayvalues:
        messagebox.showerror("Error Message", "Please type your birth day between [1-31]!")
    elif sboxday.get() == "Day":
        messagebox.showerror("Error Message", "Please choose your birth day!")        

    #Birth Month
    elif len(sboxmonth.get()) == 0:
        messagebox.showerror("Error Message", "Please don't leave your birth month empty!")
    elif sboxmonth.get() not in monthvalues:
        messagebox.showerror("Error Message", "Please type your birth month between [January-December]!")
    elif sboxmonth.get() == "Month":
        messagebox.showerror("Error Message", "Please choose your birth month!")
    elif sboxmonth.get() in thirtyone and sboxday.get() not in dayvalues[1:32]:
            messagebox.showerror("Error Message", ("Please type your birth day correctly for " + sboxmonth.get()))
    elif sboxmonth.get() in thirty and sboxday.get() not in dayvalues[1:31]:
            messagebox.showerror("Error Message", ("Please type your birth day correctly for " + sboxmonth.get()))
    elif sboxmonth.get() in twentynine and sboxday.get() not in dayvalues[1:30]:
            messagebox.showerror("Error Message", ("Please type your birth day correctly for " + sboxmonth.get()))
                
    #Birth Year
    elif len(sboxyear.get()) == 0:
        messagebox.showerror("Error Message", "Please don't leave your birth year empty!")
    elif sboxyear.get() not in yearvalues:
        messagebox.showerror("Error Message", "Please type your birth year between [1900-2015]!")
    elif sboxyear.get() == "Year":
        messagebox.showerror("Error Message", "Please choose your birth year!")

    #Gender
    elif len(gendervar.get()) <= 1:
        messagebox.showerror("Error Message", "Please select your gender!")

    #Email
    elif len(eemail.get()) == 0:
        messagebox.showerror("Error Message", "Please type your email!")
    elif "@" and "." not in eemail.get():
        messagebox.showerror("Error Message", "Please type your email correctly!")

    #Password
    elif len(epwd.get()) == 0:
        messagebox.showerror("Error Message", "Please type your password!")
    elif len(epwd.get()) <6 :
        messagebox.showerror("Error Message", "Please enter at least 6 characters in password!")

    #Retype Password
    elif len(erpwd.get()) == 0:
        messagebox.showerror("Error Message", "Please retype your password!")
    elif erpwd.get() != epwd.get():
        messagebox.showerror("Error Message", "Password didn't match! Please retype your password correctly!")
    
    else:
        tl = Toplevel(width=200, height=200)
        tl.title("User Details")

        
        detailsVars = StringVar()
        detailsVars.set(
            str("First Name: " + str(efname.get())) + "\n" +
            str("Last Name: " + str(elname.get())) + "\n" +
            str("Birthday: " + str(sboxday.get()) + " " + str(sboxmonth.get()) + " " + str(sboxyear.get())) + "\n" +
            str("Gender: " + str(gendervar.get())) + "\n" +
            str("Email: " + str(eemail.get()))
            )
        details = Label(tl, textvariable=detailsVars)
        details.grid()

        
        pwdVar1 = StringVar()
        pwdVar1.set("Password: ******")

        pwdVar2 = StringVar()
        pwdVar2.set(str("Password: " + str(epwd.get())))

        details_lpwd = Label(tl, textvariable=pwdVar1)
        details_lpwd.grid()

        
        def hidefunc():
            details_lpwd.config(textvariable=pwdVar1)
            showpwd.config(text="Show password", command=showfunc)

        def showfunc():
            details_lpwd.config(textvariable=pwdVar2)
            showpwd.config(text="Hide password", command=hidefunc)
        
        showpwd = Button(tl, text="Show password", command=showfunc)
        showpwd.grid(row=6, column=20)

b = Button(fbutton, text="Sign Up", bg='#00cc00', fg="white", command=signup)
b.pack()
b.config(font=("Helvetica Neue", 10, "bold"))


Label(root).pack() #empty space line


root.title("Sign Up")
