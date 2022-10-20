def swap_columns_and_print_matrix(matrix, swap_col_1, swap_col_2, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == matrix[i][swap_col_1]:
                matrix[i][swap_col_1], matrix[i][swap_col_2] = matrix[i][swap_col_2], matrix[i][swap_col_1]
                break


    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()


n, m = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))

matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]
temp_list = list(map(int, input("Введите два номера столбцов для обмена цифрами через пробел: ").split()))
swap_col_1, swap_col_2 = temp_list[0], temp_list[1]

swap_columns_and_print_matrix(matrix, swap_col_1, swap_col_2, n, m)