# Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)