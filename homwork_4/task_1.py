#задание 1
import sys
if len(sys.argv)<4:
    print('Введите все переменные: количество часов, оклад и премию ')
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    result = a*b+c
    print(result)
