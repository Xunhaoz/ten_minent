def strsort():
    rawstring = input("輸入字串： ")
    rawlist =list(rawstring)
    rawlist.sort()
    return "".join(rawlist)


print(strsort())
