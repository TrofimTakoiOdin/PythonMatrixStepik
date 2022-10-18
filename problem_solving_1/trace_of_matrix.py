def trace_of_matrix(matrix, n):
    total = 0
    for rows in range(n):
        for cols in range(n):
            if rows == cols:
                total += matrix[rows][cols]
    return total

n = int(input("Введите размерность квадратной матрицы одним числом: "))
matrix = []
for i in range(n):
    temp = [int(num) for num in input("Элементы матрицы на одной строке через пробел: ").split()]
    matrix.append(temp)

print(f'След матрицы равен: {trace_of_matrix(matrix, n)}')