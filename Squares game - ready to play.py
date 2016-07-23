from tkinter import *
root = Tk()
root.title("Squares")
import random
import winsound

board = Frame(root)
board.pack()

def move_left(event):
    char_coords = 125,400, 175,450
    canvas.coords(char, char_coords)

def move_right(event):
    char_coords = 325,400, 375,450
    canvas.coords(char, char_coords)

canvas = Canvas(board, width=500, height=500, bg='black')
canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)
canvas.pack(side=LEFT)
canvas.focus_set()

left = 125, 50, 175, 100
right = 325, 50, 375, 100
side = left, right

obj_coords = random.choice(side)
obj = canvas.create_rectangle(obj_coords, fill='red')
obj_coords = canvas.coords(obj)

char = canvas.create_rectangle(125,400, 175,450, fill='green')

info = Label(board, width=30, height=20, bg='black', fg='gold', font='Courier',
             text="Press Up key to start")
info.pack()

score = 0

def move():
    try:
        global obj_coords
        global score
        if obj_coords == [125.0, 500.0, 175.0, 550.0] or obj_coords == [325.0, 500.0, 375.0, 550.0]: #bottom
            winsound.Beep(1000, 100)
            score = score + 10
            score_text = "+10 points!" + "\n" + "Total score: " + str(score)
            info.config(text=score_text)
            obj_coords = random.choice(side)
            canvas.coords(obj, obj_coords)
            move()
        
        elif canvas.coords(obj) == canvas.coords(char): #clash
            winsound.Beep(1000, 500)
            clash_text = "Oops! you got hit! \n Total score: " + str(score)
            info.config(text=clash_text)
            clash_coords = canvas.coords(obj)
            canvas.delete(ALL)
            canvas.create_rectangle(clash_coords, fill='blue')
        
        else: #keep moving
            winsound.Beep(800, 100)
            obj_coords = [obj_coords[0], obj_coords[1]+50, obj_coords[2], obj_coords[3]+50]
            canvas.coords(obj, obj_coords)
            root.after(100, move)
    except:
        pass

def start(event):
    try:
        move()
    except:
        pass
    
canvas.bind('<Up>', start)
