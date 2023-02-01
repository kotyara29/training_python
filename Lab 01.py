# Task 1

print("Число четное" if int(input("Введите число: ")) % 2 == 0 else "Число нечетное")

# Task 2

print("Начинается с заглавной" if input("Введите слово")[0].isupper() == True else "Не начинается с заглавной")

# Task 3

price = int(input("Напишите цену за 1 кг"))
for i in range(1, 11):
    print(price * i)