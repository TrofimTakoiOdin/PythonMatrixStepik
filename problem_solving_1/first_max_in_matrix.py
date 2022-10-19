def print_matrix():
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(6), end='')
        print()


n, m = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]

max_value = max(max(matrix, key=max))

for i in range(n):
    if max_value in matrix[i]:
        print(i, matrix[i].index(max_value))
        break


