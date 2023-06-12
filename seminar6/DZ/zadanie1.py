# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("write first element: "))
d = int(input("write difference: "))
n = int(input("write amount of elements: "))
an = a1+d
my_list = []
for i in range(n):
    an = a1 + i * d
    my_list.append(an)
print('\n'.join(map(str, my_list)))