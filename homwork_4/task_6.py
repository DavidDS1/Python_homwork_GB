#задание 6
import sys
from itertools import count
from itertools import cycle

a = int(sys.argv[1])
j=1
for i in count(a):
    print(i)
    if j == 10:
        break
    j +=1
my_list = ['G', 'B', 1, 2]
b = float(sys.argv[2])
c=1
for el in cycle(my_list):
    print(my_list[0])
    print(my_list[1])
    print(my_list[3])
    if c == b:
        break
    c += 1
