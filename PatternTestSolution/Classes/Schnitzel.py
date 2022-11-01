import Interfaces.IDish as IDish

class Schnitzel(IDish):
    def getPrice(self):
        return 6.99
    def printDescription(self):
        return "Nices Schnitzel"