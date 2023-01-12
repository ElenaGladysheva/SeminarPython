# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt
def Discriminant(a,b,c):
    d = b ** 2 - 4 * a * c
    with open ("discr.txt","w", encoding="utf-8") as my_file:
        
        if a:
            my_file.write(f"{a}x² + {b}x + {c} = 0 \n")
            if d > 0:
                x1 = (-b + sqrt(d)) / (2 * a)
                x2 = (-b - sqrt(d)) / (2 * a)
                my_file.write(f"{x1}, {x2} \n")
            elif d == 0:
                x = -b /(2 * a)
                my_file.write(f"{x} \n")
            else:
                my_file.write("No roots! \n")
        else:
            my_file.write("The equation is incorrect! \n")


Discriminant(2,3,1)

