# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
line = input("write line: ").split()
result = {}
for i in line:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        result[i] = result.get(i, 0) + 1
        print(i, end=' ')