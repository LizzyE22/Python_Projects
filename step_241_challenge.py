

#parent class
class Wine:
    def __init__(self, region, grape):
        self.region = region
        self.grape = grape


    def myFunc(self):
        print("This is a " + self.grape)


#child class
class red_wine(Wine):
        vessel = "French oak"
        grape = "Pinot Noir"

def myFunc1(self):
        print("Thisis a red wine")


if __name__ == "__main__":

    w = Wine("Oregon", "Chardonnay")
    w.myFunc()

    r = red_wine
    r.myFunc1()
    
