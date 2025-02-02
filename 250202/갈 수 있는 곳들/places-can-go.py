from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[False] * n for _ in range(n)]
deq = deque()
count = 0
for point in points:
    x, y = point[0] - 1, point[1] - 1
    visited[x][y] = True
    deq.append((x, y))
    count += 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

while len(deq):
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            visited[nx][ny] = True
            deq.append((nx, ny))
            count += 1

print(count)