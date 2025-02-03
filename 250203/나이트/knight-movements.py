from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

step = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
deq = deque()
visited[r1][c1] = True
is_possible = False
deq.append((r1, c1))

dx, dy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n) or visited[x][y]:
        return False
    return True

while len(deq):
    x, y = deq.popleft()
    if x == r2 and y == c2:
        is_possible = True
        break
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            step[nx][ny] = step[x][y] + 1
            visited[nx][ny] = True
            deq.append((nx, ny))

if is_possible:
    print(step[r2][c2])
else:
    print(-1)