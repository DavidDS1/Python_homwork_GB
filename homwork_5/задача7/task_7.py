import json
result_dict = {}
result_list = []
pos_count, pos_sum = 0,0
with open('test_task_7.txt', 'r') as data_file:
    data_lines = data_file.readlines()
    for line in data_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        result_dict.update({data[0]: profit})
        if profit >0:
            pos_count+=1
            pos_sum+=profit
average_profit =pos_sum/pos_count
# print(average_profit)
result_list.append([result_dict, {'average_profit': average_profit}])
print(result_list)
with open ('result_json.json', 'w') as data_json:
    json.dump(result_list, data_json)
