# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint
coins = []
length = int(input("write number of coins: "))
for i in range(length):
    coins.append(randint(0,1))
print(coins)
count = 0
count2 = 0
for i in range(len(coins)):
    if coins[i] == 1:
        count += 1
    else:
        count2 += 1
sumOfcoins = 0
if count > count2:
    sumOfcoins = length - count
    print(sumOfcoins)
else:
    sumOfcoins = length - count2
    print(sumOfcoins)

