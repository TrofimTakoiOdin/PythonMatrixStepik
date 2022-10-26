def is_magic(matrix, n):
    main_diagnal, secondary_diagnal = [], []
    matrix_copy = []
    for c in matrix:
        matrix_copy.extend(c)
    for i in range(1, (n ** 2) + 1):
        if i in matrix_copy:
            return False
    first_elem = sum(matrix[0])
    for i in range(1, n):
        if (sum(matrix[i]) != first_elem) or (sum([row[i] for row in matrix]) != first_elem):
            return False
    for i in range(n):
        for j in range(n):
            if i == j:
                main_diagnal.append(matrix[i][j])
            if j == n - i - 1:
                secondary_diagnal.append(matrix[n - i - 1][i])
    if sum(main_diagnal) != first_elem or sum(secondary_diagnal) != first_elem:
        return False
    return True


n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if is_magic(matrix, n) is not True:
    print("NO")
else:
    print("YES")