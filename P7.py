def rot13():
    rawword = input("輸入一個單字")
    answer = ""
    for i in rawword:
        answer += chr((ord(i) - 65 + 13) % 26 + 65)
    return answer


print(rot13())
