
import shutil
import os

#set where the source of the files are
source = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/hold_file/'

#set the destination path to folderB
destination = '/Users/Esque/OneDrive/Documents/GitHub/Python_Projects/Python_challenges.py/receive_file/'
files = os.listdir(source)

#copying content of source file to destination file
shutil.copyfile('source', 'destination')
