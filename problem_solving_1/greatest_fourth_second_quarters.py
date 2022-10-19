n = int(input("Введите размер квадратной матрицы числом: "))
matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]
max_value = -1000000
for i in range(n):
    for j in range(n):
        if ((i >= j) and (i <= n - 1 - j)) or ((i <= j) and (i >= n - 1 - j)) or (i == j):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]

print(max_value)