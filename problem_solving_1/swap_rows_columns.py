def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
def print_matrix_swap_rows_columns(matrix, n, m, width=1):
    for r in range(m):
        for c in range(n):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()

def matrix_gen(n, m):
    matrix = [[input("Введите элемент матрицы: ") for _ in range(m)] for _ in range(n)]
    return matrix

n, m = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
matrix = matrix_gen(n, m)
print_matrix(matrix, n, m, width=1)
print()
print_matrix_swap_rows_columns(matrix, n, m, width=1)