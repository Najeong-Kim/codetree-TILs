import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [[1] * n for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def run(x, y):
    global arr
    global result
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            if arr[nx][ny] < arr[x][y] + 1:
                arr[nx][ny] = arr[x][y] + 1
                run(nx, ny)

for i in range(n):
    for j in range(n):
        run(i, j)

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, arr[i][j])
print(result)