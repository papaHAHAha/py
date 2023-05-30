# Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером
from random import randint
my_list = []
for i in range(10):
    my_list.append(randint(0,10))
print(my_list)
count = 0
for i in range(len(my_list)- 1):
    if my_list[i] < my_list[i+1]:
        count += 1
print(count)
