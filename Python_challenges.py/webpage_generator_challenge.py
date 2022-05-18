
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser



def UserTab(self):
    NewTab = "file:///C:/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/webpage_newtab_challenge.html"
    webbrowser.open_new_tab(NewTab)

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #define our master frame configuration
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550, 250))
        self.master.title('New Webpage')
        self.master.config(bg='lightgreen')

        self.button1 = Button(self.master, text = "CLICK HERE", width = 25, command=lambda:UserTab(self))
                               
        self.button1.grid( row = 2, column = 2, columnspan = 2, padx = 15, pady = 15, sticky = W+E+N+S)

   







       
if __name__ == "__main__":
 root = tk.Tk()
 App = ParentWindow(root)
 root.mainloop()
