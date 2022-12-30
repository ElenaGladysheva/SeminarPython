#Семинар 1

# 1.Напишите программу, которая проверяет является ли одно число квадратом другого
def ControlSquare ():
    a = int(input("Input the first number: "))
    b = int(input("Input the second number: "))

    if a == b**2 or b == a**2:
        print("Yes")
    else:
        print("No")

ControlSquare()
