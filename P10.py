def mysum(*arg):
    if not arg:
        return arg
    answer = arg[0]
    for i in arg[1:]:
        answer += i
    return answer


print(mysum("dasa", "sada"))
