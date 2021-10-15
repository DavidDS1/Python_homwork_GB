#задание 2
users_list = input('Введите элементы списка: ').split()
print(users_list)
el = 0
for i in range(int(len(users_list)/2)):
    users_list[el], users_list[el+1]=users_list[el+1], users_list[el]
    el+=2
print(users_list)
