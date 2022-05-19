
import shutil
import os

#set where the source of the files are
source = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/folderA'

#set the destination path to folderB
destination = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/folderB'
files = os.listdir(source)

for i in files:
        #we are saying move the files represented by 'i' to their new destination
        shutil.move(source+i, destination)
