#задание 3
def user_func (name, surname, year_of_birth, city, email, phone):
    result = f'имя - {name}, фамилия - {surname}, год рождения - {year_of_birth},' \
             f' город проживания - {city}, email - {email}, телефон {phone}'
    return print(result)
users_n =input('Ваше имя: ')
users_s = input('Ваша фамилия: ')
users_y = input('Год рождения: ')
users_c = input('Город проживания: ')
users_e = input('Ваш email: ')
users_p = input('Введите ваш телефон: ')

print(user_func(name=users_n, surname=users_s,year_of_birth= users_y, city= users_c, email= users_e, phone= users_p))
