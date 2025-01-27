n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
first = [1, 0, 3, 2]
second = [3, 2, 1, 0]
result = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(4):
    for j in range(n):
        dir, x, y = i, 0, 0
        time = 1
        if i == 0:
            x, y = j, n - 1
        elif i == 1:
            y = j
        elif i == 2:
            x = j
        elif i == 3:
            x, y = n - 1, j
        while True:
            time += 1
            if grid[x][y] == 1:
                dir = first[dir]
            elif grid[x][y] == 2:
                dir = second[dir]
            now_x, now_y = x + dx[dir], y + dy[dir]
            if not in_range(now_x, now_y):
                break
            x, y = now_x, now_y
        result = max(result, time)

print(result)