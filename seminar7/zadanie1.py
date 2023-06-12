# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте:
# вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
import random
print(type_list := [(random.randint(1,4), random.randint(1,4)) for _ in range(10)])

type_list = list(filter(lambda x: x[0] != x[1], type_list))
print(type_list := list(set(type_list)))

new_list = list(map(lambda x: 3.14 * x[0] * x[1], type_list))
print(new_list)

for i in type_list:
    if i[0] * i[1] * 3.14 == max(new_list):
        print(i, max(new_list))
        break