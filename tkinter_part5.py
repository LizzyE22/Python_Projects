from tkinter import *


win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

v.set("this is set by the program")

win = Tk()
lb = Listbox(win, height = 3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
