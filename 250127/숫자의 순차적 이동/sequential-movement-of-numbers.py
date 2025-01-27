n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_index(number):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == number:
                return (i, j)

def find_max(x, y):
    max_x, max_y, max_value = 0, 0, 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if not in_range(nx, ny):
            continue
        if grid[nx][ny] > max_value:
            max_x, max_y, max_value = nx, ny, grid[nx][ny]
    return (max_x, max_y, max_value)

for i in range(m):
    for j in range(1, n * n + 1):
        x, y = find_index(j)
        max_x, max_y, max_value = find_max(x, y)
        grid[max_x][max_y] = grid[x][y]
        grid[x][y] = max_value

for elem in grid:
    print(*elem)        
