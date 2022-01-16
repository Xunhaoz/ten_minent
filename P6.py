def pl_sentence():
    rawstring = input("輸入英文： ")
    rawstring = rawstring.split()
    answer = []
    for i, j in enumerate(rawstring):
        if rawstring[i][0] == 'a' or rawstring[i][0] == 'e' or rawstring[i][0] == 'o' or rawstring[i][0] == 'i' or rawstring[i][0] == 'u':
            answer.append(f"{rawstring[i]}way")
        else:
            answer.append(f"{rawstring[i][1::]}{rawstring[i][0]}ay")
    return answer


print(' '.join(pl_sentence()))