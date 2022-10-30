import Interfaces.ISideDish as ISideDish
import Interfaces.IDish as IDish

class Wedges(ISideDish):
    def __init__(self, Dish : IDish):
        self.__dish = Dish
    
    def getPrice(self):
        return 1.99 + self.__dish.getPrice()
    def printDescription(self):
        return "Nice wedges" + " " + self.__dish.printDescription()