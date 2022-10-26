# Магическим квадратом порядка n называется квадратная таблица размера n×n,
# составленная из всех чисел 1, 2, 3, ... n^2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.

def is_magic(matrix, n):
    main_diagnal, secondary_diagnal, matrix_copy = [], [], []
    # Выпрямляем матрицу. Первая проверка: все ли числа от 1 до N^2 есть в матрице
    # Если какая-либо проверка не пройдена, функция возвращает False
    for c in matrix:
        matrix_copy.extend(c)
    for i in range(1, (n ** 2) + 1):
        if i not in matrix_copy:
            return False
    # Вторая проверка: находим сумму первой строки, берем её за эталон, сравниваем с другими строками и столбцами
    first_elem = sum(matrix[0])
    for i in range(1, n):
        if (sum(matrix[i]) != first_elem) or (sum([row[i] for row in matrix]) != first_elem):
            return False
    # Третья проверка: сравниваем сумму элементов главной и побочной диагоналей с эталоном
    for i in range(n):
        for j in range(n):
            if i == j:
                main_diagnal.append(matrix[i][j])  # Главная диагональ
            if j == n - i - 1:
                secondary_diagnal.append(matrix[n - i - 1][i])  # Побочная диагональ
    # Что там у диагоналей?
    if sum(main_diagnal) != first_elem or sum(secondary_diagnal) != first_elem:
        return False
    # Если все проверки прошли успешно, возвращаем True!
    return True

# Считываем данные:
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
# Результат:
if is_magic(matrix, n) is not True:
    print("NO")
else:
    print("YES")