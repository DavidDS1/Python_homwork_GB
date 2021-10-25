with open('test_task_3.txt', 'r') as my_file:
    m_f = my_file.readlines()
    info_dict={}
    sum_salary = 0
    for line in m_f:
        info_str = line.split()
        info_dict.update({info_str[0]: float(info_str[1])})
        sum_salary +=float(info_str[1])
average_salary = sum_salary/len(m_f)
print(f'Средняя зарплата на этом предприятии составляет {average_salary} рублей')
print('Сотрудники получающие меньше 20000:')
for key, values in info_dict.items():
    if values < 20000:
        print(key)
