import operator


def prefix_cal(to_slove):
    operation = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    def isnumber(num):
        return num.replace('.', '').isnumeric()

    items = to_slove.split()
    while len(items) > 1:
        for i in range(len(items) - 2):
            op, num_1, num_2 = items[i:i + 3]
            if (op in operation) and isnumber(num_1) and isnumber(num_2):
                break
        items = items[:i] + [str(operation[op](float(num_1), float(num_2)))] + items[i + 3:]
    return float(items[0])


print(prefix_cal('/ * + 2 4 3 + 1 5'))
