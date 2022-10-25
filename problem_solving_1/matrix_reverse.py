n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
matrix.reverse()
for row in matrix:
    print(*row)
