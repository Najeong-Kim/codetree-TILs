n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
can_visit = False

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

dx, dy = [1, 0], [0, 1]

def move(x, y):
    global visited
    global can_visit

    if can_visit:
        return

    if x == n - 1 and y == m - 1:
        can_visit = True
        return
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            visited[nx][ny] = True
            move(nx, ny)

move(0, 0)

if can_visit:
    print(1)
else:
    print(0)