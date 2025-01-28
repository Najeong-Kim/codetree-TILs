n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

explode_list = [
    [
        [-2, -1, 1, 2],
        [0, 0, 0, 0]
    ],
    [
        [-1, 0, 1, 0],
        [0, 1, 0, -1]
    ],
    [
        [-1, -1, 1, 1],
        [-1, 1, 1, -1]
    ]
]

bomb_list = []
result = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_list.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def run(number, count):
    global grid
    global result
    if number == len(bomb_list):
        result = max(result, count)
    else:
        x, y = bomb_list[number]
        for i in range(len(explode_list)):
            dx, dy = explode_list[i]
            added = 0
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if not in_range(nx, ny):
                    continue
                if not grid[nx][ny]:
                    added += 1
                grid[nx][ny] += 1
            run(number + 1, count + added)
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if not in_range(nx, ny):
                    continue
                grid[nx][ny] -= 1

run(0, len(bomb_list))
print(result)