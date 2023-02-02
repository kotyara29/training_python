# Task 1

print("Число четное" if int(input("Введите число: ")) % 2 == 0 else "Число нечетное")

# Task 2

print("Начинается с заглавной" if input("Введите слово: ")[0].isupper() == True else "Не начинается с заглавной")

# Task 3

price = int(input("Напишите цену за 1 кг: "))
for i in range(1, 11):
    print(price * i)

price2 = int(input("Напишите цену для цикла while: "))
kilos = 1
while kilos <= 10:
    print(price2 * kilos)
    kilos += 1

# Task 4 (taken from Svyatoslav)

def calculate_pi(n=0):
    result = 3
    for i in range(n + 1):
        if i:
            delta = ((-1) ** (i + 1)) * 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
            print(delta)
            result += delta
    return result


for i in range(5):
    print(calculate_pi(i))

# Task 5

import random

name = input("Введите свое имя: ")
poryadok = ["первая", "вторая", "третья"]
number = random.randint(1, 10)
total_attempts = 3
print("Угадайте число от 1 до 10. У вас три попытки.")
for i in range(3):
    total_attempts -= 1
    attempt = int(input("Введите число: "))
    if attempt > number:
        print(
            f"Ошибка. Ваша {poryadok[i]} попытка неверна. Подсказка: задуманное число меньше {attempt}. Осталось попыток: {total_attempts}")
    elif attempt < number:
        print(
            f"Ошибка. Ваша {poryadok[i]} попытка неверна. Подсказка: задуманное число больше {attempt}. Осталось попыток: {total_attempts}")
    if attempt == number:
        print("Поздравляю! Вы угадали число!")
    elif total_attempts == 0:
        print("Ошибка. Попыток больше нет. Игра окончена")

# Task 6

import random

matrix = [[random.randrange(0, 10) for y in range(3)] for x in range(4)]
summa = 0
max_elem = 0
min_second_column = 0
for i in range(len(matrix)):
    summa += sum(matrix[i])
    if max_elem < max(matrix[i]):
        max_elem = max(matrix[i])

print(matrix)
print(summa)
print(max_elem)
print(sum(matrix[0]))
print(min(matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1]))


# Task 7

name_list = []
while True:
    name = input()
    if name == "END" or name == "end":
        break
    else:
        name_list.append(name)

# сделаем словарь из массива
dict_from_array = {i : name_list.count(i) for i in name_list}
for key, value in dict_from_array.items():
    print(key, "-", value)


