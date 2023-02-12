# Task 6

import random
def matrix_calculations():
    matrix = [[random.randrange(0, 11) for y in range(3)] for x in range(4)]
    summa = 0
    max_elem = 0
    min_second_column = 0
    for i in range(len(matrix)):
        summa += sum(matrix[i])
        if max_elem < max(matrix[i]):
            max_elem = max(matrix[i])

    print(f"Сгенерированная матрица: {matrix}")
    print(f"Сумма всех чисел матрицы составляет {summa}")
    print(f"Максимальное число в матрице - {max_elem}")
    print(f"Сумма чисел в первой строке матрицы - {sum(matrix[0])}")
    print(f"Минимальный элемент во втором столбце матрицы - {min(matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1])}")
    print(f"Максимальный элемент по главной диагонали - {max(matrix[0][0], matrix[1][1], matrix[2][2])}")

matrix_calculations()