import tkinter as tk
import mp3play
from time import sleep
import re

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Text-to-speech")
        self.master.iconbitmap("assets/icon.ico")

        self.txtVar = tk.StringVar()
        self.lbl = tk.Label(self.master, textvariable=self.txtVar, background="indigo", foreground="gold", font=("Courier", 16))
        self.lbl.pack()
        self.txtVar.set("Type words in the phrases folder")

        self.txt = tk.Text(self.master, height=10, width=40, background="lightblue", foreground="red", font=("Papyrus", 20))
        self.txt.pack()

        self.btn = tk.Button(self.master, text="EXECUTE", command=self.fn, cursor="hand2", foreground="Navy", font="Courier")
        self.btn.pack()

    def fn(self):
        self.txtGotten = self.txt.get(0.0, "end")
        self.txtStripped = self.txtGotten.strip()
        self.txtLowered = self.txtStripped.lower()
        self.txtRegexed = re.sub('[^a-z ]+', '', self.txtLowered)
        self.wordList = self.txtRegexed.split()
        
        for i in self.wordList:
            self.filename = "phrases/" + i + ".mp3"
            try:
                print("Now playing: " + i + ".mp3")
                self.track = mp3play.load(self.filename)
                self.track.play()
                sleep(self.track.seconds() + 0.4)
            except:
                print("NO SUCH FILE FOUND.")

root = tk.Tk()
myapp = App(root)
