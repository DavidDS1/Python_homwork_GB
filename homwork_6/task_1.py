#задание 1
import time
class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 5}
    def running (self):
        result_dict = self.__color
        j = 1
        while j!=5:
            for k, v in result_dict.items():
                print(k)
                time.sleep(result_dict.setdefault(k))
            j += 1
        return ' '


trfl = TrafficLight()
print(trfl.running())

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