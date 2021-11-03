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
