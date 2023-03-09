# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list=[random.randint(0, 10) for i in range(int(input("Введите количество элементов списка: ")))]
print(list)

min_num = int(input('Введите минимальное число: '))
max_num = int(input('Введите максимальное число: '))

for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        print(i)