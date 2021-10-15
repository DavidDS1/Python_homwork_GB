#задание 4
users_number = int(input('Введите число: '))
a= users_number%10
list=[]
while users_number>0:
    a = users_number % 10
    users_number = users_number // 10
    list.append(a)
result = max(list)
print(f'Самая большая цифра в вашем числе равна {result}')
