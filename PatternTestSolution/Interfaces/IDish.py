from abc import ABC, abstractmethod


class IDish:
    @abstractmethod
    def getPrice(): raise NotImplementedError
    def printDescription(): raise NotImplementedError
