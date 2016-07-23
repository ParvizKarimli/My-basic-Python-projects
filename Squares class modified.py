from tkinter import *

import random
import winsound

class Game:
    def __init__(self, master):
        self.master = master
        master.title("Squares class")

        self.board = Frame(master)
        self.board.pack()

        self.canvas = Canvas(self.board, width=500, height=500, bg='black')
        self.canvas.pack(side=LEFT)

        self.left_coords = 125, 50, 175, 100
        self.right_coords = 325, 50, 375, 100
        self.side = self.left_coords, self.right_coords

        self.obj_coords = random.choice(self.side)
        self.obj = self.canvas.create_rectangle(self.obj_coords, fill='red')
        self.obj_coords = self.canvas.coords(self.obj)

        self.char = self.canvas.create_rectangle(125,400, 175,450, fill='green')

        self.info = Label(self.board, width=30, height=20, bg='black', fg='red', font='Courier',
                          text="Press Start button to start")
        self.info.pack()

        self.score = 0

        self.canvas.focus_set()
        self.canvas.bind("<Left>", self.move_left)
        self.canvas.bind("<Right>", self.move_right)
        
        self.start_button = Button(self.board, text="Start",
                                   width=10, height=2,
                                   bg='black', fg='red', font="Courier",
                                   cursor="hand2", command=self.start)
        self.start_button.pack()

    def move_left(self, event):
        char_coords = 125,400, 175,450
        self.canvas.coords(self.char, char_coords)

    def move_right(self, event):
        char_coords = 325,400, 375,450
        self.canvas.coords(self.char, char_coords)

    def move(self):
            try:
                if self.obj_coords == [125.0, 500.0, 175.0, 550.0] or self.obj_coords == [325.0, 500.0, 375.0, 550.0]: #bottom
                    winsound.Beep(1000, 100)
                    self.score += 10
                    score_text = "+10 points!" + "\n" + "Total score: " + str(self.score)
                    self.info.config(text=score_text)
                    self.obj_coords = random.choice(self.side)
                    self.canvas.coords(self.obj, self.obj_coords)
                    self.move()

                elif self.canvas.coords(self.obj) == self.canvas.coords(self.char): #clash
                    winsound.Beep(1000, 500)
                    self.start_button.config(text="Restart", command=self.restart)
                    clash_text = "Oops! you got hit! \n Total score: " + str(self.score)
                    self.info.config(text=clash_text)
                    clash_coords = self.canvas.coords(self.obj)
                    self.canvas.delete(ALL)
                    self.canvas.create_rectangle(clash_coords, fill="blue")

                else: #keep moving
                    winsound.Beep(800, 100)
                    self.obj_coords = [self.obj_coords[0], self.obj_coords[1]+50, self.obj_coords[2], self.obj_coords[3]+50]
                    self.canvas.coords(self.obj, self.obj_coords)
                    self.after_id = root.after(25, self.move)
            except:
                pass
    
    def start(self):
        self.start_button.config(text="Pause", command=self.pause)
        self.move()

    def pause(self):
        print("Paused")
        if self.move is not None:
            root.after_cancel(self.after_id)
        self.start_button.config(text="Start", command=self.start)

    def restart(self):
        self.master.destroy()
        master = Tk()
        game = Game(master)
        

root = Tk()

game = Game(root)
