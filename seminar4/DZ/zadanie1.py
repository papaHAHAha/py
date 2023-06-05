# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
set1 = set()
set2 = set()
n = int(input("write length for first set: "))
m = int(input("write length for second set: "))
for i in range(n):
    set1.update([int(input("for first set - write only 1 element(and press enter): "))])
for i in range(m):
    set2.update([int(input("for second set - write only 1 element(and press enter): "))])
print(f'sum of two sets: {set1.union(set2)}')