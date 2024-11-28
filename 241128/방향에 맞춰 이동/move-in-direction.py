x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

N = int(input())
for i in range(N):
    direction, count = input().split()
    count = int(count)
    if direction == 'E':
        x, y = x + dx[0] * count, y + dy[0] * count
    elif direction == 'S':
        x, y = x + dx[1] * count, y + dy[1] * count
    elif direction == 'W':
        x, y = x + dx[2] * count, y + dy[2] * count
    elif direction == 'N':
        x, y = x + dx[3] * count, y + dy[3] * count

print(x, y)