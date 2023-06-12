# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
def same_by(func, list_obj: list) -> bool:
    result = []
    for obj in list_obj:
        result.append(func(obj))
    if len(set(result)) == 1:
        return True
    return False

print(same_by(lambda x:x%2 == 0, [2,4,6,8,10]))