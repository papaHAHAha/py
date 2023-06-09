# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

num = int(input("write number: "))
dict_ = dict()
for i in range(1, num + 1):
    sum_ = 0
    for j in range(1, i // 2 + 1):
        if not i % j:
            sum_ += j
    dict_[i] = sum_
dict_2 = dict()
for k, v in dict_.items():
    for k1, v1 in dict_.items():
        if k == v1 and k1 == v and k != k1 and k1 not in dict_2.keys():
            dict_2[k] = k1
print(dict_2)
sum_div_num = {}

# for number in range(1, 10000):
#     sum_ = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum_ += i
#     sum_div_num[number] = sum_
#
#
# for num in sum_div_num:
#     if num == sum_div_num.get(sum_div_num.get(num)) and num > sum_div_num.get(num):
#         print(num, sum_div_num.get(num))

