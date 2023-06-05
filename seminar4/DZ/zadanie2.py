# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
am_bush = int(input("write amount of bushes: "))
bushes = []
for i in range(am_bush):
    berries = int(input("write amount of berries on bush: "))
    bushes.append(berries)

harvested_berries = []
for j in range(len(bushes) - 1):
    harvested_berries.append(bushes[j-1] + bushes[j] + bushes[j+1])
harvested_berries.append(bushes[-2] + bushes[-1] + bushes[0])
print(max(harvested_berries))