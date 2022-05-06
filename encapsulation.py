
# This is a protected variable
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 30
print(obj._protectedVar)

# This is a private variable

class Protected:
    def __init__(self):
        self.__privateVar = 20

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()
