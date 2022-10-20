def is_square_matrix_symmetrical(matrix, n):
    flag = True
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                flag = False
                return flag
    return flag

n = int(input("Введите количество строк: "))

matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(n)]
if is_square_matrix_symmetrical(matrix, n) is True: print("YES")
else: print("NO")