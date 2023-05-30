# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
from random import randint
lis1 = []
length = int(input("write list length: "))
for i in range(length):
    lis1.append(randint(0,10))
print(lis1)
lis1 = set(lis1)
print(lis1)
print(len(lis1))