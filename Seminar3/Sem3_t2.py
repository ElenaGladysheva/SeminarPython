# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.
from random import sample

def Spisok (count, word = "abc"):
    my_list = []
    for i in range(count):
        temp = sample(word, k=3)
        my_list.append("".join(temp))
    return my_list

list_1 = Spisok(int(input("Введите количество слов в списке: ")))
print(list_1)

def IndexSecondFind (word, new_list):
    if word in new_list and new_list.count(word) > 1:
        index_1 = new_list.index(word)
        print(new_list.index(word, index_1+1))
    else:
        print("-1")

IndexSecondFind(input("Введите искомое слово:" ), list_1)
