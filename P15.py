dic = {}


def record_rainfall():
    while city := input("Please input city: "):
        if rain := input("Please input rain: "):
            rain = int(rain)
        else:
            rain = 0
        dic[city] = dic.get(city, 0) + rain
    answer = ''
    for k, i in dic.items():
        answer += f'{k:7s}: {i:2d}mm\n'
    return answer


print(record_rainfall())
