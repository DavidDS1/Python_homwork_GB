#задание 6
a=5
b=15
list=[]
while a<b:
    a=a+a*0.1
    list.append(a)
result =len(list)+1
print(f'на {result} день спортсмен пробежит более 15 км')
