
nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four':'Четыре'}


with open('test_task_4.txt') as file_1, open('test_task_4_1.txt', 'w') as new_file:
    my_str = file_1.readlines()
    for line in my_str:
        my_list = line.split()
        rus_nums = str(nums.get(my_list[0]))
        new_file.write(f'{line.replace(my_list[0], rus_nums)}')
