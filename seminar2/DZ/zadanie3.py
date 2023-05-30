# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
number = int(input("write number: "))
degree = 1
while degree < number:
    print(f'{degree} ')
    degree *= 2
