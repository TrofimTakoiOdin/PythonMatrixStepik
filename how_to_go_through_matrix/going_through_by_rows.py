# Чтобы перебрать элементы матрицы, необходимо использовать вложенные циклы.
# Например, выведем на экран все элементы матрицы, перебирая их по строкам:
rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

matrix  = [[2, 3, 1, 0],
           [9, 4, 6, 8],
           [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()

# Результатом работы такого кода будет:
#
# 2 3 1 0
# 9 4 6 8
# 4 7 2 7