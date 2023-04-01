def analytics():
    f = open('logs.log', 'r')

    def by_date():
        counter = 0
        date_to_see = input("Enter the date you want to check (format - dd-mm-yyyy): ")
        for line in f:
            if date_to_see in line:
                counter += 1
        print(f"Number of passengers crossed the border on this date is {counter}")

    def count_inland():
        inland_counter = 0
        for line in f:
            if "Inland" in line:
                inland_counter += 1
                print(line)
        print(inland_counter)

    def count_air():
        air_counter = 0
        for line in f:
            if "Air" in line:
                air_counter += 1
        print(air_counter)

    select_option = input("Press 1 to see number of inland passengers: \n"
                          "Press 2 to see number of air passengers: \n"
                          "Press 3 to see number of passengers at the specific date: ")
    if select_option == "1":
        count_inland()
    elif select_option == "2":
        count_air()
    elif select_option == "3":
        by_date()
    else:
        print("The end")

analytics()