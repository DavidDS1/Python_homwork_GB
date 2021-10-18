#задание 5

def sum_func (users_str, end_sum):
    users_list = users_str.split()
    sum_list = 0
    for i in users_list:
        if i == end_sum:
            break
        sum_list += int(i)
    return sum_list

end = 'stop'
finished = False
s =0
while not finished:
    users_str_1 = input('Введите числа через пробел: ')
    s += sum_func(users_str_1, end)
    finished = end in users_str_1
    print(f'Сумма введенных чисел равна {s}')
