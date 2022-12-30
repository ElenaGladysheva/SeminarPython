# 4. Написать программу, которая показывает первую часть дробного числа

def FractionalPart ():
    n = float(input("Input your number: "))
    num = (n * 10 % 10)
    print(int(num))

FractionalPart()

