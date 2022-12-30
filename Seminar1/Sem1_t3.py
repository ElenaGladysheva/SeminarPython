
# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
def PrintN():
    n = int(input("Input number n: "))
    print(*range(-n,n+1))

PrintN()

