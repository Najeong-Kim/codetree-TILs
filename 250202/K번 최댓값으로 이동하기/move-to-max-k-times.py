from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y, value):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] >= value:
        return False
    return True

for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    deq = deque()
    visited[r][c] = True
    deq.append((r, c))
    next_num = 0
    next_x, next_y = 100, 100
    while len(deq):
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny, grid[r][c]):
                visited[nx][ny] = True
                deq.append((nx, ny))
                if next_num == grid[nx][ny]:
                    if next_x > nx or (next_x == nx and next_y > ny):
                        next_x, next_y = nx, ny
                if next_num < grid[nx][ny]:
                    next_num = grid[nx][ny]
                    next_x, next_y = nx, ny
    if next_num != 0:
        r, c = next_x, next_y
    else:
        break

print(r + 1, c + 1)
