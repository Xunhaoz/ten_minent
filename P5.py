def pig_latin():
    answer = ""
    rawstring = input("輸入英文： ")
    if rawstring[0] == "a":
        answer = rawstring + "way"
    elif rawstring[0] == "e":
        answer = rawstring + "way"
    elif rawstring[0] == "e":
        answer = rawstring + "way"
    elif rawstring[0] == "e":
        answer = rawstring + "way"
    elif rawstring[0] == "e":
        answer = rawstring + "way"
    else:
        answer = rawstring[1::] + rawstring[0] + "ay"

    return answer


print(pig_latin())