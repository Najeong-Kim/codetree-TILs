n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0
result_k = 0

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def can_go(x, y, k):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    return True

def move(x, y):
    global visited
    global count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            move(nx, ny)

for k in range(1, 100):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                count += 1
                visited[i][j] = True
                move(i, j)
    if result < count:
        result = count
        result_k = k

print(result_k, result)
