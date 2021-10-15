#Задание 1
print('Hello, World')

name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
yes= f'Добро пожаловать, {name}, вам {age} лет, вы можете посещать наш сайт!'
no = f'Приветствуем вас, {name}, вам {age} лет, и вам запрещен доступ на наш сайт!'
wow = f'Вау-вау, дед {name}, вам {age} лет, ну и шалун вы!'
if age >=18 and age <80:
    print(yes)
elif age >=80:
    print(wow)

else:
    print(no)
