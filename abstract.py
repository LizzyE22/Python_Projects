

from abc import ABC, abstractmethod
class wine(ABC):

# passing in an argument
    @abstractmethod
    def variety(self):
        pass

class PinotNoir(wine):
# overriding abstract method
# implementing flavor profile for Pinot Noir from it's parent variety class
    def variety(self):
        print("I taste earthy and like red berries and cherries")

# implementing flavor profile for Chardonnay from it's parent variety class
class Chardonnay(wine):
    def variety(self):
        print("I taste like citrus, and stone fruits")


P = PinotNoir()
P.variety()
C = Chardonnay()
C.variety()
        

