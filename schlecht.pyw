from tkinter import *

win = Tk()
win.geometry("270x100")
win.resizable(False, False)
win.title("SCHLECHT")
win.config(bg="black")

l1 = Label(text="Opfer, Schlecht", font=(40), bg="black", foreground="red")
l1.place(x=75, y=40)

mainloop()