import tkinter as tk
from tkinter import messagebox
import time
import winsound as ws
import os

class App:
    
    # Counter labels part starts here:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Study Minutes Counter")
        self.master.geometry("-200+50")
        self.master.minsize(500, 500)
        self.master.iconbitmap("mainicon.ico")
        self.master.protocol("WM_DELETE_WINDOW", self.onMainWinDel)

        self.logSaveClickState = 'unclicked' # Log save popup window state

        # Toolbar (Menus) labels part starts here:

        self.menuBar = tk.Menu(self.master)
        self.master.config(menu=self.menuBar)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Save to log", command=self.saveLogFn)
        self.fileMenu.add_command(label="Open log", command=self.openLogFn)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.onMainWinDel)

        self.controlMenu = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Control", menu=self.controlMenu)
        self.controlMenu.add_command(label="Start counter", command=self.startFn)
        self.controlMenu.add_command(label="Pause counter", command=self.pauseFn, state="disabled")
        self.controlMenu.add_separator()
        self.controlMenu.add_command(label="Set alarm", command=self.setAndCountFn)
        self.controlMenu.add_command(label="Cancel alarm", command=self.stopCountFn, state="disabled")

        # Toolbar (Menus) labels part starts here.

        self.timeVar = tk.StringVar()
        self.timeVar.set(time.asctime())

        self.timeLabel = tk.Label(self.master, textvariable=self.timeVar,
                                  bg="black", fg="red", font=("Courier", 40), relief="groove", bd=5)
        self.timeLabel.pack(fill="both", expand="1")

        self.currentMinVal = 0

        self.totalMinVal = 0

        self.currentTxt = tk.StringVar()
        self.currentTxt.set("Current: " + str(self.currentMinVal) + " minute")

        self.currentLabel = tk.Label(self.master, textvariable=self.currentTxt,
                                     bg="black", fg="red", font=("Courier", 20))
        self.currentLabel.pack(fill="both", expand="1")

        self.totalTxt = tk.StringVar()
        self.totalTxt.set("Total: " + str(self.totalMinVal) + " minute")

        self.totalLabel = tk.Label(self.master, textvariable=self.totalTxt,
                                   bg="black", fg="red", font=("Courier", 20))
        self.totalLabel.pack(fill="both", expand="1")

        self.startButton = tk.Button(self.master, text="Start Minute Counter", command=self.startFn, bg="red",
                                     fg="black", cursor="hand2", font=("Courier", 20), relief="raised", bd=5)
        self.startButton.pack(fill="both", expand="1")

        self.timeUpdateFn()

        self.separatorLabel = tk.Label(self.master, height=2, bg="white")
        self.separatorLabel.pack(fill="both", expand="1")

        # Counter labels part finishes here.

        # Alarm labels part starts here:

        self.vcmd = self.master.register(self.validFn)
        self.timeBox = tk.Spinbox(self.master, bg="black", fg="red", font=("Courier", 20), insertbackground="red", 
                                  validate="key", validatecommand=(self.vcmd, "%P"), from_=0, to=9)
        self.timeBox.pack(fill="both", expand="1")
        self.timeBox.focus_set()

        self.txtVar = tk.StringVar()
        self.txtVar.set("Set a time for alarm")
        self.alarmLabel = tk.Label(self.master, textvariable=self.txtVar, bg="black", fg="red", font=("Courier", 20))
        self.alarmLabel.pack(fill="both", expand="1")

        self.alarmButton = tk.Button(self.master, text="Set Alarm", command=self.setAndCountFn, bg="red", fg="black",
                                     cursor="hand2", font=("Courier", 20), relief="raised", bd=5)
        self.alarmButton.pack(fill="both", expand="1")

        # Alarm labels part finishes here.

    # Counter functions part starts here:

    def timeUpdateFn(self):
        self.timeVar.set(time.asctime())
        self.master.after(1, self.timeUpdateFn)

    def startFn(self):
        try:
            if self.currentMinVal == 0 or self.currentMinVal == 1:
                self.currentTxt.set("Current: " + str(self.currentMinVal) + " minute")
            else:
                self.currentTxt.set("Current: " + str(self.currentMinVal) + " minutes")
            self.currentMinVal += 1
            
            self.startId = self.master.after(60000, self.startFn)
            
            self.startButton.config(text="Pause counter", command=self.pauseFn,
                                    bg="lime")
            
            self.controlMenu.entryconfig("Start counter", state="disabled")
            self.controlMenu.entryconfig("Pause counter", state="normal")
        except:
            pass

    def pauseFn(self):
        try:
            self.master.after_cancel(self.startId)
            
            self.totalMinVal += self.currentMinVal - 1
            if self.totalMinVal == 0 or self.totalMinVal == 1:
                self.totalTxt.set("Total: " + str(self.totalMinVal) + " minute")
            else:
                self.totalTxt.set("Total: " + str(self.totalMinVal) + " minutes")
            
            self.currentMinVal = 0
            
            self.startButton.config(text="Start counter", command=self.startFn,
                                    bg="red")
            
            self.controlMenu.entryconfig("Pause counter", state="disabled")
            self.controlMenu.entryconfig("Start counter", state="normal")

            self.saveLogFn()
        except:
            pass

    def onMainWinDel(self):
        ws.PlaySound('SystemQuestion', ws.SND_ALIAS)
        answer = tk.messagebox.askyesno(title="Closing the program",
                                        message="Are you sure you want to quit the program (log will be saved)?",
                                        default="no")
        if answer == True:
            self.saveLogFn()
            self.master.destroy()
        else:
            pass

    # Toolbar (Menus) File menu functions part starts here:
    
    def saveLogFn(self):
            try:
                oldLogObj = open('LOGS.txt', 'r')
                oldLogTxt = oldLogObj.read()
                oldLogObj.close()
                newLogObj = open('LOGS.txt', 'w')
                newLogObj.write(oldLogTxt + '\n' + str(time.asctime()) + "; " +
                              str(self.currentTxt.get()) + "; " +
                              str(self.totalTxt.get()) + '.\n')
                newLogObj.close()

                self.saveLogPopupFn()
            except:
                newLogObj = open('LOGS.txt', 'w')
                newLogObj.write(str(time.asctime()) + "; " + 
                                str(self.currentTxt.get()) + "; " + 
                                str(self.totalTxt.get()) + '.\n')
                newLogObj.close()

                self.saveLogPopupFn()

    def saveLogPopupFn(self):
        if self.logSaveClickState == 'unclicked':
            self.logSaveClickState = 'clicked'
            self.saveInfoWin = tk.Toplevel(self.master, bg="black")
            self.saveInfoWin.overrideredirect(True)
            self.saveInfoWin.attributes('-topmost', True)
            self.saveInfoWin.geometry('+%d+%d' % (self.master.winfo_rootx(), self.master.winfo_rooty()))
            self.alphaVar = 1

            self.saveInfoMsg = tk.Label(self.saveInfoWin, text="Log saved",
                                        font=('Courier', 25), bg="black", fg="white")
            self.saveInfoMsg.pack()
            
            self.saveTransFn()

    def saveTransFn(self):
        if self.alphaVar < 0:
            self.saveInfoWin.destroy()
            self.logSaveClickState = 'unclicked'
        else:
            self.alphaVar -= 0.01
            self.saveInfoWin.attributes('-alpha', self.alphaVar)
            self.saveInfoWin.geometry('+%d+%d' % (self.master.winfo_rootx(), self.master.winfo_rooty()))
            self.idTrans = self.master.after(20, self.saveTransFn)

    def openLogFn(self):
        try:
            os.startfile('LOGS.txt')
        except:
            tk.messagebox.showinfo("Log File Info", "No log file yet")

    # Toolbar (Menus) File functions part finishes here.

    # Counter functions part finishes here.

    # Alarm functions part starts here:

    def validFn(self, value):
        try:
            value = int(value)
            return True
        except:
            return False

    def setFn(self):
        self.counterVar = int(self.timeBox.get())

    def countFn(self):
        self.startId2 = self.master.after(60000, self.countFn)
        if self.counterVar > 0:
            if self.counterVar == 1:
                self.txtVar.set("< " + str(self.counterVar) + " minute remained to alarm")
            else:
                self.txtVar.set("< " + str(self.counterVar) + " minutes remained to alarm")
            self.counterVar -= 1
        else:
            self.stopCountFn()
            self.notifWin = tk.Toplevel(self.master)
            self.notifWin.title("Alarm Notification")
            self.notifWin.iconbitmap("alarmicon.ico")
            self.notifWin.state("zoomed")
            self.notifWin.protocol("WM_DELETE_WINDOW", self.onNotifWinDel)
            self.notifWin.transient(self.master)
            self.notifWin.attributes("-topmost", True)
            self.notifWin.focus_force()
            
            self.alarmColor = "blue"
            self.alarmFn()

            self.notifLabel = tk.Label(self.notifWin, text="Time is up!",
                                       font=("Courier", 150), bg="red", fg="blue")
            self.notifLabel.pack(expand="1")

            self.alarmButton.config(state="disabled")

    def setAndCountFn(self):
        try:
            self.alarmButton.config(text="Cancel alarm", command=self.stopCountFn,
                                    bg="lime")

            self.setFn()

            self.countFn()
            
            self.controlMenu.entryconfig("Set alarm", state="disabled")
            self.controlMenu.entryconfig("Cancel alarm", state="normal")
        except:
            pass

    def stopCountFn(self):
        try:
            self.alarmButton.config(text="Set alarm", command=self.setAndCountFn,
                                    bg="red")
            self.counterVar = 0
            self.txtVar.set("Set a time for alarm")
            self.master.after_cancel(self.startId2)
            
            self.controlMenu.entryconfig("Cancel alarm", state="disabled")
            self.controlMenu.entryconfig("Set alarm", state="normal")
        except:
            pass

    def alarmFn(self):
        if self.alarmColor == "red":
            self.alarmColor = "blue"
        else:
            self.alarmColor = "red"

        self.notifWin.config(bg=self.alarmColor)

        ws.Beep(1000, 500)
        
        self.notifWin.after(50, self.alarmFn)

    def onNotifWinDel(self):
        self.alarmButton.config(state="normal")
                        
        try:
            self.controlMenu.entryconfig("Cancel alarm", state="disabled")
            self.controlMenu.entryconfig("Set alarm", state="normal")
        except:
            pass
        
        self.notifWin.destroy()

    # Alarm functions part finishes here.

root = tk.Tk()
myApp = App(root)
root.mainloop()
