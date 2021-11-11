#задание 3
class OurOneException (Exception):
    def __init__(self, text):
        self.text = text
class OurTwoException (Exception):
    def __init__(self, text_1):
        self.text = text_1
el_list = input('вводите элементы списка: ')
my_list = []
while el_list !='stop':
    el_list = input('вводите элементы списка: ')
    try:
        if el_list.isdigit():
            my_list.append(el_list)
        elif el_list == 'stop':
            raise OurTwoException ('вы завершили ввод элементов списка')
        else:
            raise OurOneException('Вы ввели не число')
    except OurOneException as e:
        print(e)
    except OurTwoException as d:
        print(d)
print(my_list)

