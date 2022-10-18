import numpy
matrix = [list(map(int, input("Введите числа через пробел: ").split())) for i in range(int(input("Введите размер квадратной матрицы числом: ")))]
means = [numpy.mean(matrix[i]) for i in range(len(matrix))]
for rows in range(len(matrix)):
    counter = 0
    for cols in range(len(matrix)):
        if matrix[rows][cols] > means[rows]:
            counter += 1
    print(counter)