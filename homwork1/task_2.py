#задание 2
time_users = int(input('Введите время в секундах: '))
hours = time_users//3600
minutes = ((time_users - hours*3600)//60)
seconds =time_users - ((hours*3600)+(minutes*60))
time= f'Вы затратили на готовку {hours:02}.{minutes:02}.{seconds:02} ч'
print(time)
