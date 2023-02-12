def select_task():
    try:
        while True:
            selection = int(input("Какое задание запустить? Введите число от 1 до 7: "))
            if selection == 1:
                from Lab01.Task_1 import even_numbers
            if selection == 2:
                from Lab01.Task_2 import upper_lower
            if selection == 3:
                from Lab01.Task_3 import for_while_choice
            if selection == 4:
                from Lab01.Task_4 import call_calculate_pi
            if selection == 5:
                from Lab01.Task_5 import guess_number
            if selection == 6:
                from Lab01.Task_6 import matrix_calculations
            if selection == 7:
                from Lab01.Task_7 import border_counter
            if selection < 1 or selection > 7:
                print("Нужно выбрать задание от 1 до 7.")
                continue
            other_task = input("Продолжим? Y/N: ")
            answer_no = ("N", "n", "нет", "Нет", "НЕТ", "no", "NO", "No", "н")
            if other_task in answer_no:
                print("Нет значит нет. До свидания!")
                break
    except ValueError:
        print("Нужно ввести число от 1 до 7.")
        select_task()

select_task()
