import how_to_go_through_matrix.print_square_matrix


def matrix_diagnal_swap(matrix, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][j]
                break


n = int(input("Введите количество строк: "))
matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]
matrix_diagnal_swap(matrix, n)
how_to_go_through_matrix.print_square_matrix.print_square_matrix(matrix, n, width=1)
