#задание 1
def my_func():
    try:
        num_1 = float(input('Сколько денег на вашей карте?: '))
        num_2 = float(input('Стоимость одной булочки: '))
        result_1 = num_1 / num_2
    except ZeroDivisionError:
        return print('булочка не может стоить 0 рублей')
    return f'За ваш бюджет можно купить {result_1} булочек'
result = my_func()
print(result)
