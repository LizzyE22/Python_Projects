import os

def openFile():
    with open('text1.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()


fName = 'text1.txt'

fPath = 'C:\\Users\\Esque\\OneDrive\\Documents\\GitHub\\Python_Projects\\script_assignment.py'

dirs = os.listdir(fPath)
for file in dirs:
    print(file)


abPath = os.path.join(fPath, fName)
print(abPath)


time = os.path.getmtime(fPath)
print(time)


fName2 = 'text2.txt'

fPath2 = 'C:\\Users\\Esque\\OneDrive\\Documents\\GitHub\\Python_Projects\\script_assignment.py'

abPath2 = os.path.join(fPath2, fName2)
print(abPath2)

time2 = os.path.getmtime(fPath2)
print(time2)




if __name__ == "__ main __":
    openFile()
