    
import datetime

x = datetime.datetime.now()
print(x)

i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1


i = 0
while i < 10:
    print("{} iteration through the loop.".format(i))
    i += 1    


i = 1
while i < 9:
    print(i)
    if i == 4:
        break
    i += 1


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

for x in range(6):
    print(x)
else:
    print("Finally")
 



name = 'Python'
print(len(name))
for i in enumerate(name):
    print(i)
