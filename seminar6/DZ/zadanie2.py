# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
my_list = []
for i in range(15):
    my_list.append(randint(0, 100))
print(my_list)
minim = int(input("write min element: "))
maxim = int(input("write max element: "))
res = []
for x in range(len(my_list)):
    if minim <= my_list[x] <= maxim:
        res.append(x)
print(res)