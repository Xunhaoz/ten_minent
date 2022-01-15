def my_sum(*a, start=10):
    sumNum = start
    for i in a:
        sumNum += i
    return sumNum


print(my_sum(1, 2, 3, 5, start=50))
