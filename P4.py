def hex_to_dec():
    num = input("輸入 16 進位數字： ")
    answer = 0
    for i, j in enumerate(reversed(num)):
        i *= 1
        if j.isdigit():
            answer += int(j) * (16 ** i)
        else:
            answer += (ord(j)-55) * (16 ** i)

    return answer


print(hex_to_dec())
