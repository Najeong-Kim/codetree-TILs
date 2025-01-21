n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# Write your code here!
for command in commands:
    index, value = -1, 0
    for i in range(n):
        now = grid[i][command - 1]
        if now != 0:
            index = i
            value = now
            break
    if index == -1:
        continue
    for i in range(value):
        for j in range(4):
            x, y = index + dx[j] * i, command - 1 + dy[j] * i
            if 0 <= x < n and 0 <= y < n:
                grid[x][y] = 0
    arr = [[] for _ in range(n)]
    for i in range(n):
        now = []
        for j in reversed(range(n)):
            if grid[j][i] != 0:
                now.append(grid[j][i])
        while len(now) < n:
            now.append(0)
        now.reverse()
        for j in range(n):
            arr[j].append(now[j])
    grid = arr

for elem in grid:
    print(*elem)