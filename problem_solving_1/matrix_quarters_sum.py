n = int(input("Введите размер квадратной матрицы числом: "))
matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]
total_top, total_bottom, total_left, total_right = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            total_top += matrix[i][j]
        if i > j and i > n - 1 - j:
            total_bottom += matrix[i][j]
        if i > j and i < n - 1 - j:
            total_left += matrix[i][j]
        if i < j and i > n - 1 - j:
            total_right += matrix[i][j]
print(f"Верхняя четверть: {total_top}")
print(f"Правая четверть: {total_right}")
print(f"Нижняя четверть: {total_bottom}")
print(f"Левая четверть: {total_left}")

