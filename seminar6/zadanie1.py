# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве
from random import randint
first_list = [randint(1,9) for i in range(6)]
print(first_list)
second_list = [randint(1,9) for i in range(6)]
print(second_list)
third_list = [i for i in first_list if i not in second_list]
print(list(set(third_list)))