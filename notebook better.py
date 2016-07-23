from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.title("Notebook")
root.geometry("500x500-500+50")
root.config(bg='turquoise')

def savefunc():
    filename = asksaveasfilename(
        title="Save As",
        initialdir="D:",
        defaultextension="*.*",
        filetypes=(
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Python Files", "*.py")
        ))

    try:
        fob = open(filename, 'w')
        fob.write(text.get(0.0, "end-1c"))
        fob.close()
    except:
        pass

def openfunc():
    filename = askopenfilename(
        title="Open",
        initialdir="D:",
        filetypes=(
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Python Files", "*.py")
            )
        )

    
    try:
        with open(filename, 'r') as fob:
            text.delete(0.0, END)
            text.insert(END, fob.read())
            fob.close()
    except:
        pass


text = Text(root, bg='cyan', fg='red', font='Courier')
text.pack()

frame = Frame(root)
frame.pack()

save_button = Button(frame, text="Save", command=savefunc,
                     cursor='hand2', width=20, height=2,
                     bg='indigo', fg='gold', font='Helvetica')
save_button.pack(side=LEFT)

open_button = Button(frame, text="Open", command=openfunc,
                     cursor='hand2', width=20, height=2,
                     bg='indigo', fg='gold', font='Helvetica')
open_button.pack()

root.mainloop()
