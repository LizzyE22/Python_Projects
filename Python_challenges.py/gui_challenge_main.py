
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #define our master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550, 250))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        #browse buttons
        self.btnBrowse = Button(self.master, text='Browse...', width=15, font=("Helvetica", 10))
        self.btnBrowse.grid(row=3, column=0, columnspan=2, padx=(15,0), pady=(85,0))

        self.btnBrowse = Button(self.master, text='Browse...', width=15, font=("Helvetica", 10))
        self.btnBrowse.grid(row=4, column=0, columnspan=2, padx=(15,0), pady=(15,0))

        self.btnCheck = Button(self.master, text='Check for files...', width=15, height=2, font=("Helvetica", 10))
        self.btnCheck.grid(row=5, column=0, columnspan=2, padx=(15,0), pady=(25,0))

        #text field buttons
        self.txtblank = Entry(self.master, width=60)
        self.txtblank.grid(row=3, column=2, padx=(15,0), pady=(80,0))

        self.txtblank = Entry(self.master, width=60)
        self.txtblank.grid(row=4, column=2, padx=(15,0), pady=(15,0))

        #close program button
        self.btnClose = Button(self.master, text='Close Program', width=15, height=2, font=("Helvetica", 10))
        self.btnClose.grid(row=5, column=2, sticky=SE)

        tk.filedialog.askdirectory()
        def callback():
            name= fd.askdirectory()
            print(name)

        errmsg = 'Error!'
        self.btnCheck(self.master, text='Check for files...', command=callback).grid


if __name__ == "__main__":
 root = tk.Tk()
 App = ParentWindow(root)
 root.mainloop()
