def sum_number(L):
    return sum([int(i) for i in L.split() if i.isdigit()])


print(sum_number("45 sad 58 55zsad 54asd5 554f 1"))
