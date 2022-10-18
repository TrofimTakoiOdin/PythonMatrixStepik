# Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:

def print_square_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()