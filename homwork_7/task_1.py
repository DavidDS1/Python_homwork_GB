from random import randint

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
    def __str__(self):
        print('вызван метод стр')
        s=''
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                s+=f'{self.my_list[i][j]:02} '
            s+='\n'
        return s
    def __add__(self, other):
        print('вызван метод адд')
        result_list = [[ self.my_list[i][j]+other.my_list[i][j] for j in range(len(self.my_list[i]))]
                       for i in range(len(self.my_list))]
        return Matrix(result_list)

m = Matrix([[1,2,3], [4,5,6], [7,8,9]])
b = Matrix([[3,2,1], [6,5,4], [9,8,7]])
# b=Matrix([[randint(0,90) for i in range(5)] for j in range(5)])

print(m)
print(b)
print(m+b)