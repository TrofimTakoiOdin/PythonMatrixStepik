# Метод ljust()
# Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
#
# Результатом выполнения следующего кода:

print('a'.ljust(3))
print('ab'.ljust(3))
print('abc'.ljust(3))

# будет:
#
# a⎵⎵
# ab⎵
# abc

# Исходная строка не обрезается, даже если в ней больше символов, чем нужно.
#
# Результатом выполнения следующего кода:

print('abcdefg'.ljust(3))

# будет:
#
# abcdefg
# Строковый метод ljust() использует вместо пробела другой символ, если передать ему второй аргумент, необязательный.
#
# Результатом выполнения следующего кода:

print('a'.ljust(5, '*'))
print('ab'.ljust(5, '$'))
print('abc'.ljust(5, '#'))

# будет:
#
# a****
# ab$$$
# abc##

# Применив метод ljust() для выравнивания столбцов при выводе таблицы мы получим следующий код:

rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов

matrix  = [[277, -930, 11, 0],
           [9, 43, 6, 87],
           [4456, 8, 290, 7]]

for r in range(rows):
    for c in range(cols):
        print(str(matrix[r][c]).ljust(6), end='')
    print()

# Результатом выполнения такого кода будет:
#
# 277   -930  11    0
# 9     43    6     87
# 4456  8     290   7
