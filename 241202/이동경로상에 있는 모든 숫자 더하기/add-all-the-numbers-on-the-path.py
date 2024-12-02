N, T = map(int, input().split())
path = input()
roads = []
for _ in range(N):
    road = list(map(int, input().split()))
    roads.append(road)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = N // 2, N // 2
d = 0
count = roads[x][y]
is_return = False

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for i in range(T):
    command = path[i]
    if command == 'F':
        nx, ny = x + dx[d], y + dy[d]
        if not in_range(nx, ny):
            continue
        else:
            x, y = nx, ny
            count += roads[x][y]
    if command == 'R':
        d = (d + 1) % 4
    if command == 'L':
        d = (d + 3) % 4

print(count)