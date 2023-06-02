# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
my_list = []
countOfElements = int(input("write amount of elements: "))
for i in range(countOfElements):
    my_list.append(randint(0, 10))
print(my_list)
number = int(input("write x: "))
count = 0
for x in my_list:
    if number == x:
        count += 1
print(f'X meets {count} times')