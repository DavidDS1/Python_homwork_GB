with open('test_fl.txt', 'w') as my_file:
    str_users = input('Введите данные: ')
    my_file.writelines(f'{str_users} \n')
    while str_users != '':
        str_users = input('Введите данные: ')
        my_file. writelines(f'{str_users} \n')
