# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
ticket = int(input("Write ticket number: "))
Ticket1 = int(ticket / 1000)
Ticket2 = ticket % 1000
def threedigit(ticket):
    x1 = ticket % 10
    x2 = ticket % 100 // 10
    x3 = ticket // 100
    return x1 + x2 + x3
a = threedigit(Ticket1)
b = threedigit(Ticket2)
if a == b:
    print("ticket is lucky")
else:
    print("ticket is not lucky :(")



