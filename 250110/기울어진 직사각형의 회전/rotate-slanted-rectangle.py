n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

a, b = r - 1, c - 1

if (dir == 0):
    temp = grid[a][b]
    for i in range(m4):
        grid[a - i][b - i] = grid[a - i-1][b - i-1]
    for i in range(m3):
        grid[a-m4 - i][b-m4 + i] = grid[a-m4 - i-1][b-m4 + i+1]
    for i in range(m2):
        grid[a-m4-m3 + i][b-m4+m3 + i] = grid[a-m4-m3 + i+1][b-m4+m3 + i+1]
    for i in range(m1):
        grid[a-m4-m3+m2 + i][b-m4+m3+m2 - i] = grid[a-m4-m3+m2 + i+1][b-m4+m3+m2 - i-1]
    grid[a - 1][b + 1] = temp
else:
    temp = grid[a][b]
    for i in range(m1):
        grid[a - i][b + i] = grid[a - i-1][b + i+1]
    for i in range(m2):
        grid[a-m1 - i][b+m1 - i] = grid[a-m1 - i-1][b+m1 - i-1]
    for i in range(m3):
        grid[a-m1-m2 + i][b+m1-m2 - i] = grid[a-m1-m2 + i+1][b+m1-m2 - i-1]
    for i in range(m4):
        grid[a-m1-m2+m3 + i][b+m1-m2-m3 + i] = grid[a-m1-m2+m3 + i+1][b+m1-m2-m3 + i+1]
    grid[a - 1][b - 1] = temp

for elem in grid:
    print(*elem)