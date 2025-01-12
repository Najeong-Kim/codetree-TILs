n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(grid[r-1][c-1]):
    for j in range(4):
        x, y = r - 1 + dx[j] * i, c - 1 + dy[j] * i
        if 0 <= x < n and 0 <= y < n:
            grid[x][y] = 0

new = [[0] * n for i in range(n)]

for i in range(n):
    arr = []
    for j in reversed(range(n)):
        if grid[j][i]:
            arr.append(grid[j][i])
    for now, v in enumerate(arr):
        new[n - 1 - now][i] = v

for elem in new:
    print(*elem)
