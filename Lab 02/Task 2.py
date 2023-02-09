def new_power(a, b):
    return a ** b


x, y = map(int, input("Введите два целых числа (через пробел): ").split())

print(f"Число {x} в степени {y} = {new_power(x, y)}")
