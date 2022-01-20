import operator


def most_repeated_letter(data):
    answerlist = []
    charlist = list(set(data))
    for i in charlist:
        answerlist.append((i, data.count(i)))
    result = sorted(answerlist, key=operator.itemgetter(1), reverse=True)[0]
    answer = f"'{result[0]}' repeat {result[1]} times"
    return answer


print(most_repeated_letter('independence'))
