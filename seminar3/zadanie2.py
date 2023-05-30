# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
from random import randint
lis1 = list()
length = int(input("write list length: "))
for i in range(length):
    lis1.append(randint(0,10))
print(lis1)
k = int(input("write indent length: "))
for i in range(k):
    lis1.insert(0, lis1.pop())
print(lis1)

