# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель
# за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
# статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
from random import randint

days = int(input('write number of days: '))
temp = 1
count = 0
count_max = 0

for i in range(days):
    temp += randint(-3, 3)
    print(temp)

    if temp > 0:
        count += 1
    else:
        count = 0
    if count_max < count:
        count_max = count
print(f'оттепель длилась {count_max}')