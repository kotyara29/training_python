def select_option():
    choice = int(input("Выберите способ расчета факториала. 1 - цикл, 2 - рекурсия: "))
    number = int(input("Введите число, факториал которого вы хотите получить: "))

    def loop_option(number):
        output = 1
        for i in range(1, number + 1):
            output *= i
        print(output)

    def recursion_option(number):
        if number == 0:
            return 1
        else:
            return number * recursion_option(number - 1)



    if choice == 1:
        loop_option(number)
    else:
        print(recursion_option(number))

select_option()

