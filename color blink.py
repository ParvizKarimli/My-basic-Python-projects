from tkinter import *
root = Tk()
root.title("Color Blink")

import random



label1 = Label(root, width=39, height=47, relief='groove')
label1.grid(row=0, column=1)

label2 = Label(root, width=39, height=47, relief='groove')
label2.grid(row=0, column=2)

label3 = Label(root, width=39, height=47, relief='groove')
label3.grid(row=0, column=3)

label4 = Label(root, width=39, height=47, relief='groove')
label4.grid(row=0, column=4)

label5 = Label(root, width=39, height=47, relief='groove')
label5.grid(row=0, column=5)



def blink():


    colors = ['blue','red','green','yellow','purple']
    
    
    color1 = random.choice(colors)
    label1.config(bg=color1)
    colors.remove(color1)
    
    color2 = random.choice(colors)
    label2.config(bg=color2)
    colors.remove(color2)
    
    color3 = random.choice(colors)
    label3.config(bg=color3)
    colors.remove(color3)
    
    color4 = random.choice(colors)
    label4.config(bg=color4)
    colors.remove(color4)
    
    color5 = random.choice(colors)
    label5.config(bg=color5)
    colors.remove(color5)
    
    
    root.after(500, blink)


blink()
