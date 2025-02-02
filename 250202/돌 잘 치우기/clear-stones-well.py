from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = [tuple(map(int, input().split())) for _ in range(k)]
rocks = []
picked_rocks = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rocks.append((i, j))

result = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y):    
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False            
    return True

def check():
    global result

    visited = [[False] * n for _ in range(n)]
    deq = deque()
    count = 0

    for i in picked_rocks:
        grid[rocks[i][0]][rocks[i][1]] = 0

    for point in points:
        x, y = point[0] - 1, point[1] - 1
        visited[x][y] = True
        deq.append((x, y))
        count += 1
    
    while len(deq):
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                deq.append((nx, ny))
                count += 1

    for i in picked_rocks:
        grid[rocks[i][0]][rocks[i][1]] = 1
    
    result = max(result, count)

def pick_rocks(index, count):
    global picked_rocks
    if count == m:
        check()
        return
    if index >= len(rocks):
        return
    
    picked_rocks.append(index)
    pick_rocks(index + 1, count + 1)
    picked_rocks.pop()

    pick_rocks(index + 1, count)

pick_rocks(0, 0)
print(result)