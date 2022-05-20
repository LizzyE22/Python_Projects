
import shutil
import os
import os.path
from os import path
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd



def SourceBrowse(root):
    file_path = fd.askdirectory()
    userEntry1.insert(END, file_path)

def DestBrowse(root):
    file_path = fd.askdirectory()
    userEntry2.insert(END, file_path)

def checkDir(root):
    path.exists("Python_Projects/")
    file_path = fd.askdirectory()
    checkFile.insert(END, file_path)

    
#frame configuration
root = Tk()
root.title('File Transfer')
root.geometry("700x350")
root.config(bg='black')

#set where the source of the files are
source = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/hold_file/'

#set the destination path 
destination = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/receive_file/'
files = os.listdir(source)

#set directory path
directory = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/'


for file in files:
    #gets the absolute path of the file, which includes the source folder path and the file name
    absolutePath = source + file
    #moves the file located at the absolute path to the destination folder
    shutil.copy(absolutePath, destination)


#first button to choose source file
root.SourceBrowse = Button(root, text="Browse Files and Choose Folder", command=lambda:
                           checkDir(root))
root.SourceBrowse.grid(row = 1, column = 1, padx = 15, pady = 35)

#second button to choose destination file
root.DestBrowse = Button(root, text="Choose Folder to Receive File(s)", command=lambda:
                         DestBrowse(root))
root.DestBrowse.grid(row = 2, column = 1, padx = 15, pady = 65)

#check if file exists button
root.btnCheck = Button(root, text="Check if File Exists", command=lambda:
                       SourceBrowse(root))
root.btnCheck.grid(row = 3, column = 1, padx = 15, pady = 15)

#first text field
userEntry1 = Entry(root, width = 75)
userEntry1.grid(row = 1, column = 2)

#second text field
userEntry2 = Entry(root, width = 75)
userEntry2.grid(row = 2, column = 2)

#third text field for checking if file exists
checkFile = Entry(root, width = 75)
checkFile.grid(row = 3, column = 2)





root.mainloop()

