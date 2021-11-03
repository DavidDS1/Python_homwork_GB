#задание 2
class Road:
    def __init__(self,_length, _width):
        self._length=_length
        self._width=_width
    def weight (self):
        result_weight =self._length * self._length*25*5
        weight_ton = result_weight/1000
        return print(f'{weight_ton} тонн')
materials= Road(1000, 10)
materials.weight()
