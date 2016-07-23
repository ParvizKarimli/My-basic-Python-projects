from tkinter import *
root = Tk()
root.title("Time & Date")

import time

txtvar = StringVar()
txtvar.set("")
label = Label(root, textvariable=txtvar, width=30, height=5, relief='groove', bd=10,
             font=('Courier', 50), bg='indigo', fg='gold',)
label.pack()

def refreshfunc():
    #start
    timedateobj = time.localtime()
    day = str(timedateobj.tm_mday)
    month = str(timedateobj.tm_mon)
    year = str(timedateobj.tm_year)
    hour = str(timedateobj.tm_hour)
    minute = str(timedateobj.tm_min)
    second = str(timedateobj.tm_sec)
    day_of_year = str(timedateobj.tm_yday)
    day_of_week = timedateobj.tm_wday

    if len(day) == 1:
        day = "0" + str(day)

    if len(month) == 1:
        month = "0" + str(month)

    if len(hour) == 1:
        hour = "0" + str(hour)

    if len(minute) == 1:
        minute = "0" + str(minute)

    if len(second) == 1:
        second = "0" + str(second)

    if day_of_week == 0:
        day_of_week = "Monday"
    elif day_of_week == 1:
        day_of_week = "Tuesday"
    elif day_of_week == 2:
        day_of_week = "Wednesday"
    elif day_of_week == 3:
        day_of_week = "Thursday"
    elif day_of_week == 4:
        day_of_week = "Friday"
    elif day_of_week == 5:
        day_of_week = "Saturday"
    else:
        day_of_week = "Sunday"

    current = hour + ":" + minute + ":" + second + "\n" + day + "." + month + "." + year + "\n" + day_of_week + "\n" + "The " + day_of_year + "th day of the year"
    #finish
    txtvar.set(current)
    root.after(1, refreshfunc)

refreshfunc()
