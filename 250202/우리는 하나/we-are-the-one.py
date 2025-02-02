from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

picked_cities = []
result = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def can_go(x, y, value, visited):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or not (u <= abs(grid[x][y] - value) <= d):
        return False
    return True

def check():
    global result

    visited = [[False] * n for _ in range(n)]
    deq = deque()
    count = 0

    for city in picked_cities:
        x, y = city[0], city[1]
        visited[x][y] = True
        deq.append((x, y))
        count += 1
    
    while len(deq):
        x, y = deq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny, grid[x][y], visited):
                visited[nx][ny] = True
                deq.append((nx, ny))
                count += 1
    result = max(result, count)

def pick_cities(index, count):
    global picked_cities
    if count == k:
        check()
        return
    if index >= n * n:
        return
    
    picked_cities.append((index // n, index % n))
    pick_cities(index + 1, count + 1)
    picked_cities.pop()

    pick_cities(index + 1, count)

pick_cities(0, 0)
print(result)