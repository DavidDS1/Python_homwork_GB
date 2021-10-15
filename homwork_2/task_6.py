#задание 6
total_amount = int(input('Введите количесвто исследуемых товаров: '))
goods = []
number=1
while number<= total_amount:
    names = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    amount = input('Введите количество товара: ')
    units = input('Введите еденицы измерения: ')
    goods.append((number, {'names': names, 'prices': price,
                          'amount': amount, 'units': units}))
    number+=1
# print(goods)
result = {}
for i, j in goods:
    for key, value in j.items():
        if not result.get(key):
            result[key]=[value]
        else:
            result[key].append(value)
for key, value in result.items():
    result[key]= list(set(value))
print(result)