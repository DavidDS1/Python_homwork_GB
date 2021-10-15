#задание 4
users_str = input('напишите предложение из 5 слов: ').split()
# print(users_str)
j=1
for i in users_str:
    result = i
    print(f'{j}.{result[:10].title()}')
    j+=1
