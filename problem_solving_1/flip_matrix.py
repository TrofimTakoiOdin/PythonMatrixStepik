n,i = int(input()), 0
matrix = [list(map(int, input().split())) for i in range(n)]
matrix.reverse()
while i!= n:
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()
    i += 1
