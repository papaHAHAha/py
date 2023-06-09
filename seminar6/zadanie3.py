# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
from random import randint
min_ = 1
max_ = 9
my_list = [randint(min_, max_) for i in range(6)]
print(my_list)
count = 0
for i in set(my_list):
    count += my_list.count(i) // 2
print(count)