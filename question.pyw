from tkinter import *

win = Tk()
win.geometry("300x150")
win.title("Böses Geometry Dash")
win.resizable(False, False)


MB = Menu(win)
win.config(menu=MB)

#Windows 2 (OuterSpace)

def OuterSpace():
    print("Outer Space")

    win1nope = Tk()
    win1nope.geometry("300x150")
    win1nope.title("Böses Geometry Dash > ERROR")
    win1nope.resizable(False, False)

    def win1nope_OK():
        print("OK")
        
    def win1nope_DOCH():
        b3.config(bg="#3CFF00", text="OK", command=win1nope_OK)

    l2 = Label(win1nope, text="Nicht Schwer genug!!!")
    l2.pack()

    b2 = Button(win1nope, text="OK", bg="#3CFF00", command=win1nope_OK)
    b2.place(x=30, y=30, width=100, height=100)

    b3 = Button(win1nope, text="DOCH!", bg="#FF0000", command=win1nope_DOCH)
    b3.place(x=160, y=30, width=100, height=100)

def Help():
    print("HELP")
    b1.config(text="Magmatic Sanctuary", command=MagmaticSanctuary)

def MagmaticSanctuary():
    print("YES")
    fh = open('questionfile.QF', 'w')
    fh.write("MagmaticSancturay")
    fh.close()

    l3.config(foreground="#3CFF00")


Menu = Menu(win, tearoff=0)
MB.add_cascade(label='Options', menu=Menu)
Menu.add_command(label='Help', command=Help)

l1 = Label(text="Wählen sie ein Nerviges GD Level:")
l1.pack()

b1 = Button(text="Magmatic Sanctuary", command=MagmaticSanctuary)
b1.place(x=25, y=30, width=120, height=27)

b1 = Button(text="Outer Space", command=OuterSpace)
b1.place(x=155, y=30, width=120, height=27)

l3 = Label(text="Gut Gemacht!", foreground="#F0F0F0")
l3.place(x=110, y=100)

mainloop()
#NOOO 69 PLS NOOOO AAAAAAHHHH