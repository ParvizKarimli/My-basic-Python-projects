import tkinter as tk
import tkinter.filedialog
import mp3play
import os

class Player:
    def __init__(self, master):
        self.master = master
        master.title("Rad MP3 Player")
        master.geometry("300x300+300+50")
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        master.iconbitmap("rad player icon.ico")
        master.config(bg="yellow")

        self.uiFrame = tk.Frame(master, bg="#0099ff",
                                width="100")
        self.uiFrame.pack(side="bottom", fill="both")
        
        self.trackNameVar = tk.StringVar()
        self.trackNameVar.set("Choose a song to play")
        self.trackNameLabel = tk.Label(self.uiFrame, textvariable=self.trackNameVar,
                                       bg="#0099ff", fg="yellow",
                                       font="Courier")
        self.trackNameLabel.pack(fill="both")

        self.btnFrame = tk.Frame(self.uiFrame)
        self.btnFrame.pack(fill="both")
        
        self.addimgVar = tk.PhotoImage(file="ejectbutton.png")
        self.addBtn = tk.Button(self.btnFrame, image=self.addimgVar,
                                command=self.addFunc, bg="#0099ff", cursor="hand2")
        self.addBtn.pack(side="left", expand=1, fill="both")
        
        self.playimgVar = tk.PhotoImage(file="playbutton.png")
        self.playBtn = tk.Button(self.btnFrame, image=self.playimgVar,
                                 command=self.playFunc, bg="#0099ff", cursor="hand2")
        self.playBtn.pack(side="left", expand=1, fill="both")

        self.pauseimgVar = tk.PhotoImage(file="pausebutton.png")

        self.stopimgVar = tk.PhotoImage(file="stopbutton.png")
        self.stopBtn = tk.Button(self.btnFrame, image=self.stopimgVar,
                                 command=self.stopFunc, bg="#0099ff", cursor="hand2")
        self.stopBtn.pack(side="left", expand=1, fill="both")

        self.volVar = tk.IntVar()
        self.volVar.set(100)
        self.volumeSlider = tk.Scale(self.uiFrame, orient="horizontal", command=self.volFunc,
                                     cursor="hand1",bg="#0099ff", fg="yellow", width=50,
                                     troughcolor="#0099ff", activebackground="#0099ff",
                                     variable=self.volVar)
        self.volumeSlider.pack(fill="both")

        self.state = ""

    def addFunc(self):
        trackPath = tk.filedialog.askopenfilename(
            title="Choose your track",
            filetypes=(
                ("Mp3 Files", "*.mp3"),
                ("All Files", "*.*")
                )
            )
        
        try:
            rootAndext = os.path.basename(trackPath)
            trackName = os.path.splitext(rootAndext)[0]
            self.trackNameVar.set(trackName)
            self.master.title(trackName)
            self.track = mp3play.load(trackPath)
            self.track.volume(self.v)
        except:
            pass

        self.playFunc()

    def playFunc(self):
        try:
            self.track.play()
            self.playBtn.config(image=self.pauseimgVar, command=self.pauseFunc)
        except:
            pass
        self.state = "restarted"

    def pauseFunc(self):
        try:
            self.track.pause()
            if self.state != "stopped":
                self.playBtn.config(image=self.playimgVar,command=self.unpauseFunc)
        except:
            pass

    def unpauseFunc(self):
        try:
            self.track.unpause()
            self.playBtn.config(image=self.pauseimgVar, command=self.pauseFunc)
        except:
            pass

    def stopFunc(self):
        try:
            self.state = "stopped"
            self.track.stop()
            self.playBtn.config(command=self.playFunc, image=self.playimgVar)
        except:
            pass

    def volFunc(self, v):
        try:
            self.v = self.volumeSlider.get()
            self.track.volume(self.v)
        except:
            pass

    def on_closing(self):
        self.stopFunc()
        self.master.destroy()
        

root = tk.Tk()
obj = Player(root)
