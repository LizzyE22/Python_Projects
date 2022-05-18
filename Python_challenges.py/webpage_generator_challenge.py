
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser



def UserTab(self):
    top = """
    <!DOCTYPE html>
    <html>
        <head>
        <meta charset="utf-8">
        </head>
        <body>
            <h1>
    """

    middle = self.textEntry.get()

    bottom = """
            </h1>
        </body>
    </html>
    """

    f = open("webpage_newtab_challenge.html", "w")
    f.write(top + middle + bottom)
    f.close()
    url = "webpage_newtab_challenge.html"
    webbrowser.open_new_tab(url)

    
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
        self.textEntry = Entry(self.master, width = 25)
        self.textEntry.grid(row = 1, column = 2, columnspan = 2, padx = (15,0), pady = (15,0), sticky = W+E+N+S)
        

    
   







       
if __name__ == "__main__":
 root = tk.Tk()
 App = ParentWindow(root)
 root.mainloop()
