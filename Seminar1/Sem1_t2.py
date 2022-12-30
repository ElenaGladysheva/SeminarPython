# 2. На вход 5 чисел, найти максимальное
def Max():
    max = 0
    for i in range(5):
        nam = int(input(f'{i+1}-number: '))
        if max < nam:
            max = nam
    print(f'{max} - max namber')

Max()

