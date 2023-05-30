# Напишите программу для печати всех уникальных значений в словаре.
my_dict = [{"V": "S001"},
           {"V": "S002"},
           {"VI": "S001"},
           {"VI": "S005"},
           {"VII": "S005"},
           {"V": "S009"},
           {"VIII": "S007"}]
my_list = list()
# for item in range(len(my_dict)):
#     my_list += list(my_dict[item].values())
# print(list(set(my_list)))
# первое решение

for item in my_dict:
    for values in item.values():
        my_list.append(values)
print(list(set(my_list)))
