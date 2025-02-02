from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

time = 0
last_melt = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_check(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y]:
        return False
    return True

while True:
    visited = [[False] * m for _ in range(n)]
    deq = deque()
    visited[0][0] = True
    deq.append((0, 0))
    melt_count = 0
    while len(deq):
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_check(nx, ny):
                visited[nx][ny] = True
                if a[nx][ny] == 1:
                    melt_count += 1
                    a[nx][ny] = 0
                else:
                    deq.append((nx, ny))
    if melt_count != 0:
        last_melt = melt_count
        time += 1
    else:
        break

print(time, last_melt)