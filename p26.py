import operator


def prefix(to_slove):
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    op, num1, num2 = to_slove.split()
    return operation[op](float(num1), float(num2))


print(prefix("+ 2 6"))
