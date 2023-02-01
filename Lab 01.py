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
attempt = input("Угадайте число от 1 до 10. У вас три попытки. Введите число: ")
for i in range(3):
    if attempt > number:
        print(f"Ошибка. Ваша {poryadok[i]} попытка неверна. Подсказка: задуманное число больше {attempt}. Попробуйте еще раз!")
        total_attempts -= 1
        print(input("Введите число: "))
    elif attempt < number:
        print(f"Ошибка. Ваша {poryadok[i]} попытка неверна. Подсказка: задуманное число меньше {attempt}. Попробуйте еще раз!")
        total_attempts -= 1
        print(input("Введите число: "))
    elif attempt == number:
        print("Поздравляю! Вы угадали число!")
    elif total_attempts == 0:
        print("Ошибка. Попыток больше нет. Игра окончена")


