def new_power():
    x, y = map(int, input("Введите два целых числа (через пробел): ").split())

    print(f"Число {x} в степени {y} = {x ** y}")

new_power()

