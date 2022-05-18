
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser



def UserTab(self):
    NewTab = "webpage_newtab_challenge.html"
    webbrowser.open_new_tab(NewTab)
    f = open("NewTab", "w")
    f.write("\n")
    self.textEntry.insert(END, f)


    #open and read the file after appending
    f = open("NewTab", "r")
    print(f.read())
    

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

        #text field buttons
        self.textEntry = Entry(self.master, text = "ENTER TEXT", width = 25)
        self.textEntry.grid(row = 1, column = 2, columnspan = 2, padx = (15,0), pady = (15,0), sticky = W+E+N+S)
        

    
   







       
if __name__ == "__main__":
 root = tk.Tk()
 App = ParentWindow(root)
 root.mainloop()
