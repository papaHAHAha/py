# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
ThreeDigitNumber = int(input("write three-digit number: "))
FirstNumber = int(ThreeDigitNumber / 100)
SecondNumber = int(ThreeDigitNumber % 100)
SecondNumber = int(SecondNumber / 10)
ThirdNumber = int(ThreeDigitNumber % 10)
Sum = FirstNumber + SecondNumber + ThirdNumber
print("the sum of a three-digit number: ", Sum)
