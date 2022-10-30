import Interfaces.IDish as IDish
class ISideDish(IDish):
    def __init__(self, Dish : IDish):
        self.__dish = Dish