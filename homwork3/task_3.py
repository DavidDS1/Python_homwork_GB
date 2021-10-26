#задание 3
def my_func (a,b, c):
    sum = a+b+c
    result = sum-min(a,b,c)
    return result
a = int(input("Введите 'a': "))
b=int(input("Введите 'b': "))
c=int(input("Введите 'c': "))
sum_a_b_c = my_func(a, b, c)
print(sum_a_b_c)



