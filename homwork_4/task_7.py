#задание7
def fact (n):
    pr = 1
    for i in range(1, n+1):
        pr = pr*i
        yield pr

for i in fact(10):
    print(i)
