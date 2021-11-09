 # реализовать функцию подсчета общего количества ткани, которое подтребуется на пошив и пальто и костюма не удалось

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumption(self):
        a = self.v / 6.5 + 0.5
        return f'Для пошива пальто нужно: {a} ткани'


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        b = 2 * self.h + 0.3
        return f'Для пошива костюма нужно: {b} ткани'






coat = Coat(54)
suit = Suit(1.73)
a = coat.fabric_consumption
b = suit.fabric_consumption
print(a)
print(b)
print(a + b)
