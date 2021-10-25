result_dict={}
with open('test_task_6.txt','r') as my_data:
    data_list=my_data.readlines()
    # print(data)
    for line in data_list:
        data = line.split()
        sum_hours=0
        for i in data[1:]:
            if i != '-':
                num = '0'
                for elem in i:
                    if elem.isdigit():
                        num+=elem
                    else:
                        break
                sum_hours += int(num)
        result_dict.update({data[0].strip(':'):sum_hours})
print(result_dict)

