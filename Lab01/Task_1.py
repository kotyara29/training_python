# Task 1
def even_numbers():
    while True:
        number = input("Введите число. Если хотите закончить, напишите СТОП: ")
        if number == "СТОП" or number == "стоп":
            print("Мы закончили.")
            break
        elif number.isdigit() == False:
            print("Вы ввели не число. Попробуйте снова.")
        elif int(number) % 2 == 0:
            print("Число четное")
        else:
            print("Число нечетное")


even_numbers()



