# #задание 5
rating_list = [10, 8, 8, 7, 5, 3, 2]
rating_number= int(input('Введите номер рейтинга участника забега: '))
j=0
for i in rating_list:
    if rating_number == i:
        rating_list.insert(j+1, rating_number)
        break
    elif rating_number>max(rating_list):
        rating_list.insert(0, rating_number)
        break
    elif rating_number<min(rating_list):
        rating_list.append(rating_number)
        break
    else:

        el = rating_number+1
        if el ==i:
            print('Хотя этот случай не рассмотрен в задаче')
            rating_list.insert(j+1, rating_number)
            break
    j+=1
print(rating_list)
