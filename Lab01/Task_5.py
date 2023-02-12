# Task 5

import random
def guess_number():
    name = input("Введите свое имя: ")
    poryadok = ["первая", "вторая", "третья"]
    number = random.randint(1, 10)
    total_attempts = 3
    print(f"{name}, угадайте число от 1 до 10. У вас три попытки.")
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
            print(f"{name}, поздравляю! Вы угадали число!")
            break
        elif total_attempts == 0:
            print(f"Ошибка. {name}, попыток больше нет. Игра окончена")

guess_number()
