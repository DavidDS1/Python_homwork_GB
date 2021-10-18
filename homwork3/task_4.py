#задание 4

def my_func (x, y):
    result= x**y
    return result
def my_func_1 (a, b):
    c=1
    for i in range(b):
        e = c*a
        c=e
    result_1 = 1/c
    return result_1

print('Решение через **')
x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
z= my_func(x, y)
print(round(z, 4))

print('Решение при помощи цикла')
a = float(input('Введите действительное положительное число: '))
b = abs(int(input('Введите целое отрицательное число: ')))
d= my_func_1(a, b)
print(round(d, 4))
