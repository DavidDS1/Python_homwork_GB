#задание 4

my_list = [2,2, 1, 3, 5, 1, 7, 8, 9, 4, 1, 9, 200, 100, 200, 3]
resul_list = [i for i in my_list if my_list.count(i) == 1]
print(resul_list)
