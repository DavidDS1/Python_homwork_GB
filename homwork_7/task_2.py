#задание 2
from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass
class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def consumption (self):
        return float(self.V/6.5 + 0.5)
    def sum_c_c (self, list_coat):
        j=0
        for i in list_coat:
            j+=i.consumption
        return j


class Costume (Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def consumption (self):
        return float(2 * self.H + 0.3)

    def sum_c_cos(self, list_costume):
        j=0
        for i in list_costume:
            j+=i.consumption
        return j

c1 = Coat(20)
c2 = Coat(15)
c3 = Coat(10)
list_coat = [c1, c2, c3]
co1 = Costume(9)
co2 = Costume(6)
co3 = Costume(3)
list_costume = [co1, co2, co3]
print(c1.consumption)
print(c2.consumption)
print(c3.consumption)
print(f'суммарный расход для пальто -  {c1.sum_c_c(list_coat)}')
print(co1.consumption)
print(co2.consumption)
print(co3.consumption)
print(f'суммарный расход для костюмов -  {co1.sum_c_cos(list_costume)}')




