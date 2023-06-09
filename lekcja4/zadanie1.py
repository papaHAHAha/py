# в списке хранятся числа. нужно выбрать только четные числа и составить список пар:
# (число;квадрат числа)
# 1 2 3 5 8 15 23 38
# [(2,4), (8,64), (38,1444)]
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []
# for i in list1:
#     if i % 2 == 0:
#         res.append((i, i**2))
#
# print(res)
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# def where(f, col):
#     return [x for x in col if f(x)]
#
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, list1)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)