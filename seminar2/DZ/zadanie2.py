# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
x = y = 0
s = int(input("введите сумму чисел: "))
p = int(input('введите произведение чисел: '))
for x in range(1000):
    x += 1
    for y in range(1000):
        y += 1
        if (x + y == s) and (x * y == p):
            print(f'X = {x}, Y = {y}')
