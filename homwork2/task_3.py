#задание 3
print('Решение через словарь')
month_1=(input('Введите № месяца: '))

season_1 = {'1': 'winter', '2': 'winter', '3': 'winter',
            '4':'spring ', '5': 'spring ', '6': 'spring ',
            '7':'summer', '8':'summer', '9':'summer',
            '10':'autumn', '11':'autumn', '12':'autumn'}
result_1 = season_1.get(month_1)
print(f'Сейчас время года - {result_1}')


print('Решение через списки')
month_2= int(input('Введите № месяца: '))
season_2 = ['winter', 'winter', 'winter',
            'spring', 'spring', 'spring',
            'summer', 'summer', 'summer',
            'autumn', 'autumn', 'autumn']
result_2 = season_2[month_2+1]
print(f'Сейчас время года - {result_2}')
