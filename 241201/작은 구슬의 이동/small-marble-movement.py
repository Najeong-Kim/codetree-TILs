n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

direction = mapper[d]

for i in range(t):
    nx, ny = r + dx[direction], c + dy[direction]
    if in_range(nx, ny):
        r, c = nx, ny
    else:
        direction = 3 - direction

print(r + 1, c + 1)