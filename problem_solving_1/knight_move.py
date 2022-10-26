def print_square_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
nums_dict = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
board = [["." for i in range(8)] for j in range(8)]
knight = input()
knight = (letters_dict.get(knight[0]), nums_dict.get(knight[1]))
board[knight[1]][knight[0]] = "N"
for i in range(8):
    for j in range(8):
        if abs((knight[0] - j) * (knight[1] - i)) == 2:
            board[i][j] = "*"
print_square_matrix(board, 8, width=1)

