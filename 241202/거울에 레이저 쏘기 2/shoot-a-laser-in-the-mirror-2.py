N = int(input())
arr = []

for _ in range(N):
    mirrors = input()
    line = []
    for mirror in mirrors:
        line.append(mirror)
    arr.append(line)

K = int(input())

count = 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
d = (K - 1) // N

if d == 0:
    x, y = 1, K
elif d == 1:
    x, y = K - N, N
elif d == 2:
    x, y = N, 3 * N - K
elif d == 3:
    x, y = 4 * N - K, 1

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

while True:
    count += 1
    if arr[x - 1][y - 1] == '/':
        d = d + 1 if d % 2 == 0 else d - 1
    else:
        d = 3 - d
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny):
        break
    else:
        x, y = nx, ny

print(count)