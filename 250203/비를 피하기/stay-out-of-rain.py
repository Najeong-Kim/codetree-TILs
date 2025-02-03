from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

humans = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            humans.append((i, j))
result = [[0] * n for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

for i in range(h):
    a, b = humans[i][0], humans[i][1]
    step = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    deq = deque()
    visited[a][b] = True
    is_possible = False
    deq.append((a, b))
    while len(deq):
        x, y = deq.popleft()
        if grid[x][y] == 3:
            is_possible = True
            result[a][b] = step[x][y]
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = True
                deq.append((nx, ny))
    if not is_possible:
        result[a][b] = -1

for elem in result:
    print(*elem)