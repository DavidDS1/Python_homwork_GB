a = '10 20 30 40 50 70 '

with open('test_task_5.txt', 'w') as my_file:
    my_file.write(a)
with open('test_task_5.txt') as nums:
    str_nums = nums.read()
    res_nums = str_nums.split()
    j=0
    for i in res_nums:
        j=j+int(i)
print(j)


