import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * n for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def run(x, y, count):
    global arr
    global result
    is_end = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            is_end = False
            if arr[x][y]:
                return arr[x][y] + 1
            return run(nx, ny, count + 1)
    if is_end:
        return count
        
for i in range(n):
    for j in range(n):
        arr[i][j] = run(i, j, 1)

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, arr[i][j])
print(result)
