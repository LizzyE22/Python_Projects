
import shutil
import os

#set where the source of the files are
source = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/hold_file/'

#set the destination path 
destination = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/'
files = os.listdir(source)

#copying content of source file to destination file
shutil.copyfile(source, destination)

for file in files:
    #gets the absolute path of the file, which includes the source folder path and the file name
    absolutePath = source + file
    #moves the file located at the absolute path to the destination folder
    shutil.copy(absolutePath, destination)




