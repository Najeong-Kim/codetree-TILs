from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
step = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
deq = deque()
visited[0][0] = True
is_possible = False
deq.append((0, 0))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or a[x][y] == 0:
        return False
    return True

while len(deq):
    x, y = deq.popleft()
    if x == n - 1 and y == m - 1:
        is_possible = True
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            step[nx][ny] = step[x][y] + 1
            visited[nx][ny] = True
            deq.append((nx, ny))

if is_possible:
    print(step[n - 1][m - 1])
else:
    print(-1)