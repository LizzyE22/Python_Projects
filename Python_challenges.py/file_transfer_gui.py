
import shutil
import os
import os.path
from os import path
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import datetime



def SourceBrowse(self):
    file_path = fd.askdirectory()
    self.txtblank1.insert(END, file_path)

def DestBrowse(self):
    file_path = fd.askdirectory()
    self.txtblank2.insert(END, file_path)

def btnCheck(self):
    source = self.txtblank1.get()
    print(source)
    files = os.listdir(source)
    dest = self.txtblank2.get()
    print(dest)
    
    #loop through the files
    #check each file to see if its newer than 24 hours ago
    #if it is, we are going to copy it to the destination
    for file in files:
        #gets the absolute path of the file, which includes the source folder path and the file name
        absolutePath = source + '/' + file
        
        #gets the modification time of the file in mtime format
        mtime = os.path.getmtime(absolutePath)
        #converts the mtime to a proper datetime format
        modTime = datetime.datetime.fromtimestamp(mtime)

        #gets the current date and time
        current = datetime.datetime.now()
        #gets the time 24 hrs ago
        twentyFour = current - datetime.timedelta(hours=24)

        #if the file was modified within the last 24 hrs, move the file
        if (modTime > twentyFour):
            shutil.copy(absolutePath, dest)

    
#frame configuration
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
        self.SourceBrowse = tk.Button(self.master, text='Browse...', width=15, font=("Helvetica", 10), command=lambda:
                                        SourceBrowse(self))
        self.SourceBrowse.grid(row=3, column=0, columnspan=2, padx=(15,0), pady=(85,0))


        #second button to choose destination file
        self.DestBrowse = tk.Button(self.master, text='Browse...', width=15, font=("Helvetica", 10), command=lambda:
                                     DestBrowse(self))
        self.DestBrowse.grid(row=4, column=0, columnspan=2, padx=(15,0), pady=(15,0))


        #check if file exists button
        self.btnCheck = Button(self.master, text='Check for files...', width=15, height=2, font=("Helvetica", 10), command=lambda:
                                    btnCheck(self))
        self.btnCheck.grid(row=5, column=0, columnspan=2, padx=(15,0), pady=(25,0))

        #first text field
        self.txtblank1 = Entry(self.master, width=60)
        self.txtblank1.grid(row=3, column=2, padx=(15,0), pady=(80,0))

        #second text field
        self.txtblank2 = Entry(self.master, width=60)
        self.txtblank2.grid(row=4, column=2, padx=(15,0), pady=(15,0))

        #close program button
        #self.btnClose = Button(self.master, text='Close Program', width=15, height=2, font=("Helvetica", 10),
                               #command=self.master.quit)
        #self.btnClose.grid(row=5, column=2, sticky=SE)







if __name__ == "__main__":
 root = tk.Tk()
 App = ParentWindow(root)
 root.mainloop()

