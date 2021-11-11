#задание 2
class MyException (Exception):
    def __init__(self, text):
        self.text = text
        print(text)

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель : '))
    if b==0:
        raise MyException('Деленеие на 0 невозможно')


    c= a/b
    print (c)
except MyException as e:
    print ('наша ошибка')
    print (e)
except Exception as d:
    print('Не наша ошибка')
    print(d)
