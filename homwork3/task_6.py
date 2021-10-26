#задание 6

def int_func (users_str):
    if users_str.islower():
        str_l = users_str.lower()
        result = str_l.title()
        return result

    return print('Введите слова маленькими латинскими буквами')


u_str = input('Введите предложение: ').split()
s_t = ' '.join(u_str)
print(int_func(s_t))
while int_func(s_t)==None:
    u_str = input('Введите предложение: ').split()
    s_t = ' '.join(u_str)
    print(int_func(s_t))



