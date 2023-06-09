# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
a = int(input("write A: "))
b = int(input("write B: "))
def exponentiate(a: int, b: int):
    if a == 0:
        return 0
    if b == 0:
        return 1
    else:
        return a * exponentiate(a, b-1)
print(exponentiate(a, b))

