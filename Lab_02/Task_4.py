import random
list_with_numbers = list(range(10))
new_list = [a + random.random() for a in list_with_numbers if a % 2]

#new_list = list(map(lambda x: x % 2, list_with_numbers))
# list_with_numbers = list(range(10))
# new_list = []
# for i in list_with_numbers:
#     if not i % 2:
#         new_list.append(i + random.random())
print(new_list)
