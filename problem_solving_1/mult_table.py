n, m = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
matrix = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end='')
    print()