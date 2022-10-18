def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

n, m = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
matrix = [[input("Введите элемент матрицы: ") for _ in range(m)] for _ in range(n)]
print_matrix(matrix, n, m, width=1)