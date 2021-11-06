#задание 3
class Cell:
    def __init__(self, param):
        self.param = param
    def __add__(self, other):
        return self.param+other.param
    def __sub__(self, other):
        if self.param - other.param >0:
            return self.param - other.param
        else:
            return Cell( f'Разность количества клеток меньше нуля')
    def __mul__(self, other):
        common_cell= self.param*other.param
        return common_cell
    def __truediv__(self, other):
        comon_cell = self.param//other.param
        return comon_cell
    def make_order(self, count):
        s=''
        for i in range (self.param//count):
            s+='*'*count +'\n'
        s+='*'*(self.param%count)
        return s
    def __str__(self):
        return f'{self.param}'


c1 = Cell(15)
c2 = Cell(20)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.make_order(6))
