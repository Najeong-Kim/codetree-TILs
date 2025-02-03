from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

walls = []
picked_walls = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((i, j))

result = 10 ** 9

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y, visited):    
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def check():
    global result

    step = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    deq = deque()
    visited[r1][c1] = True
    deq.append((r1, c1))
    now = 10 ** 9

    for i in picked_walls:
        grid[walls[i][0]][walls[i][1]] = 0

    while len(deq):
        x, y = deq.popleft()
        if x == r2 and y == c2:
            now = step[x][y]
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny, visited):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                deq.append((nx, ny))

    for i in picked_walls:
        grid[walls[i][0]][walls[i][1]] = 1
    
    result = min(result, now)

def pick_walls(index, count):
    global picked_walls
    if count == k:
        check()
        return
    if index >= len(walls):
        return
    
    picked_walls.append(index)
    pick_walls(index + 1, count + 1)
    picked_walls.pop()

    pick_walls(index + 1, count)

pick_walls(0, 0)
if result == 10 ** 9:
    print(-1)
else:
    print(result)