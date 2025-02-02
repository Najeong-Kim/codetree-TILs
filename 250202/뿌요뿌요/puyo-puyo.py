import sys
sys.setrecursionlimit(2500)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0
max_blocks = 0

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def can_go(x, y, k):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] != k:
        return False
    return True

def move(x, y):
    global visited
    global count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            count += 1
            move(nx, ny)

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        count = 1
        k = grid[i][j]
        if can_go(i, j, k):
            visited[i][j] = True
            move(i, j)
        if count >= 4:
            result += 1
        max_blocks = max(max_blocks, count)

print(result, max_blocks)
