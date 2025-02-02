n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
arr = []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def can_go(x, y):
    if not (0 <= x < n and 0 <= y < n):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def move(x, y):
    global visited
    global count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            visited[nx][ny] = True
            count += 1
            move(nx, ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            count = 1
            visited[i][j] = True
            move(i, j)
            arr.append(count)

arr.sort()
print(len(arr))
for elem in arr:
    print(elem)
