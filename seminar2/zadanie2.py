# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
A = int(input("write A number: "))
i = 2
fib1 = 1
fib2 = 1
answer = 0
while answer <= A - 2:
    answer = fib1 + fib2
    fib1 = fib2
    fib2 = answer
    i = i + 1
if answer == A:
    print(i)
else:
    print("-1")