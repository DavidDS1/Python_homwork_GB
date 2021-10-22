#задание 2
list_1 = [100,200,300,20,22,300,400,1,3,2]

a = [list_1[i] for i in range(1, len(list_1)) if list_1[i]>list_1[i-1]]
print(a)
