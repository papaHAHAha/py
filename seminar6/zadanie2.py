# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
from random import randint
my_list = [randint(1,9) for i in range(6)]
print(my_list)
count = 0
for i in range(1, len(my_list) - 1):
    if my_list[i-1] < my_list[i] and my_list[i+1] < my_list[i]:
        count += 1
print(count)