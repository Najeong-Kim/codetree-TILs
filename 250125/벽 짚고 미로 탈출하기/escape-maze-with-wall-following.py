N = int(input())
x, y = map(int, input().split())
init_x, init_y = x, y

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Write your code here!

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dir = 0
time = 0
isPossible = True

def in_range(x, y):
    return 0 < x <= N and 0 < y <= N

while True:
    new_x, new_y = x + dx[dir], y + dy[dir]
    if not in_range(new_x, new_y):
        time += 1
        break
    if grid[new_x][new_y] == '#':
        dir = (dir + 3) % 4
    else:
        x, y = new_x, new_y
        time += 1
        new_dir = (dir + 1) % 4
        right_x, right_y = x + dx[new_dir], y + dy[new_dir]
        if in_range(right_x, right_y) and grid[right_x][right_y] == '.':
            dir = new_dir
    if init_x == x and init_y == y and dir == 0:
        isPossible = False
        break

if isPossible:
    print(time)
else:
    print(-1)