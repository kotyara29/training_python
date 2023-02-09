# Task 7

name_list = []
while True:
    name = input("Кто пересекает границу? Если людей нет, введите END: ")
    if name == "END" or name == "end":
        break
    else:
        name_list.append(name)

# сделаем словарь из массива
dict_from_array = {i : name_list.count(i) for i in name_list}
for key, value in dict_from_array.items():
    print(key, "-", value)
