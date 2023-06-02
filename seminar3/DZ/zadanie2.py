# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
my_list = []
countOfElements = int(input("write amount of elements: "))
for i in range(countOfElements):
    my_list.append(randint(0, 10))
print(my_list)
number = int(input("write x: "))
minGap = abs(number - my_list[0])
gap = 0
closeNumber = 0
for j in my_list:
    gap = abs(number - my_list[j])
    if gap < minGap:
        minGap = gap
        closeNumber = j
print(my_list[closeNumber])