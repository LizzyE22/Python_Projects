
import shutil
import os

#set where the source of the files are
source = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/hold_file/hold_text.txt'

#set the destination path 
destination = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/receive_file'
files = os.listdir(source)

#copying content of source file to destination file
shutil.copyfile(source, destination)

for file in files:
    #gets the absolute path of the file, which includes the source folder path and the file name
    absolutePath = (source + 'hold_text.txt')
    #moves the file located at the absolute path to the destination folder
    shutil.copyfile(absolutePath, destination)




