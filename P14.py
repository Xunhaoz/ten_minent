dic = {
    "三明治": 50,
    "咖啡": 40,
    "沙拉": 30,
}


def order_meal():
    sum = 0
    while meal := input("Input the meal name: "):
        if meal in dic:
            sum += dic[meal]
        else:
            print("no meal")
    return f'All meal totally cost {sum} dollars'


print(order_meal())
