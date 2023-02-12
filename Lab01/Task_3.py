# Task 3
def cycle_for():
    price = int(input("Напишите цену за 1 кг: "))
    for i in range(1, 11):
        cost = price * i
        print(f"Стоимость {i} кг составляет {cost}")


def cycle_while():
    price = int(input("Напишите цену за 1 кг: "))
    kilos = 1
    while kilos <= 10:
        cost = price * kilos
        print(f"Стоимость {kilos} кг составляет {cost}")
        kilos += 1


def for_while_choice():
    choice = input("Каким способом выводить цену: FOR или WHILE? FOR - 1, WHILE - 2: ")
    if choice == 1:
        cycle_for()
    else:
        cycle_while()

for_while_choice()