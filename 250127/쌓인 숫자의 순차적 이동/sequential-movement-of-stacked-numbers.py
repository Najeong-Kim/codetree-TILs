n, m = map(int, input().split())
grid = [[] for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        grid[i].append([arr[j]])

move_nums = list(map(int, input().split()))
dx, dy = [1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_index(number):
    for i in range(n):
        for j in range(n):
            if number in grid[i][j]:
                return (i, j)

def find_max(x, y):
    mx, my, mv = 0, 0, 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            for j in grid[nx][ny]:
                if j > mv:
                    mx, my, mv = nx, ny, j
    return (mx, my)


for i in range(m):
    num = move_nums[i]
    x, y = find_index(num)
    mx, my = find_max(x, y)
    index = grid[x][y].index(num)
    grid[mx][my] = grid[x][y][:index + 1] + grid[mx][my]
    grid[x][y] = grid[x][y][index + 1:]

for i in range(n):
    for j in range(n):
        if len(grid[i][j]):
            print(*grid[i][j])
        else:
            print('None')