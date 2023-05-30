# Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка, больших предыдущего (элемента с предыдущим номером
from random import randint
mylist = []
for i in range(10):
    mylist.append(randint(0,10))
print(mylist)
count = 0
for i in range(len(mylist)- 1):
    if mylist[i] < mylist[i+1]:
        count += 1
print(count)
