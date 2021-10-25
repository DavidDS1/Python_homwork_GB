with open('test_task_2.txt', 'r') as file:
    my_file = file.readlines()
    j =0
    for num, line in enumerate(my_file):
        j+=1
        d = line.split()
        print(f'{num+1}-{len(d)}')
    print(f'количесвто строк равно {j}')
