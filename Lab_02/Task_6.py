my_list = [(1, 1, 1), (1, 2, 3), (-1, -1, 7), (-3, -2, 8), (0, 0, 0), (3, -4, -5)]
my_list_sums = my_list
my_list_third_biggest = my_list

my_list_sums.sort(key=lambda x: x[0] + x[1] + x[2])
my_list_third_biggest.sort(key=lambda x: x[2])

print(f"The list sorted by tuple sums is following: {my_list_sums}")
print(f"The list sorted by the third biggest element is following: {my_list_third_biggest}")

example_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}
example_dict_alphabet = dict(sorted(example_dict.items()))
example_dict_descending_values = dict(sorted(example_dict.items(), key=lambda x: x[1], reverse=True))

print(f"The dictionary sorted in alphabetical order is following: {example_dict_alphabet}")
print(f"The dictionary sorted by descending values is following: {example_dict_descending_values}")
