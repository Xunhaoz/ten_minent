import random


def guessing_game():
    targetNumber = random.randint(0, 100)

    while 1:
        inputNumber = input("猜猜數字 (0~99): ")
        if inputNumber.isdigit():
            inputNumber = int(inputNumber)
            if inputNumber > targetNumber:
                print("猜得太高再試一次")
            elif inputNumber < targetNumber:
                print("猜得太低再試一次")
            else:
                print("猜對了！答案是", targetNumber)
                break
        else:
            print("請輸入數字")

guessing_game()