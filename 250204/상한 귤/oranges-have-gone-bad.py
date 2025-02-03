from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

deq = deque()
result = [[-1] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
oranges = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            oranges.append((i, j))
            visited[i][j] = True
            deq.append((i, j))
            result[i][j] = 0
        if grid[i][j] == 1:
            result[i][j] = -2

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

while len(deq):
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            result[nx][ny] = result[x][y] + 1
            visited[nx][ny] = True
            deq.append((nx, ny))

for elem in result:
    print(*elem)