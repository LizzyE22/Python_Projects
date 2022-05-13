from tkinter import *

win = Tk()

b1 = Button(win, text="One")
b2 = Button(win, text="Two")

b1.pack()
b2.pack()

b1.pack(side=LEFT)
b2.pack(side=LEFT)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)

b1.pack(side = BOTTOM, padx = 15)
b2.pack(side = BOTTOM, padx = 15)

win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

l = Label(win, text="This is a label")
l.grid(row=1, column=0)


win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

b1.configure(text="Uno")

def but1():
    print("Button one was pushed")
b1.configure(command=but1)
