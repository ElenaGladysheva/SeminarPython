# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.
from random import sample

def NumFind (len_list, number):
    new_list = sample (range(1, len_list * 2), k=len_list)
    print(new_list)
    if number in new_list:
        return "Yes"
    return "No"

print(NumFind(int(input("Введите длину списка: ")), int(input("Введите искомое число: "))))
