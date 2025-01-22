n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Write your code here!
path = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

while True:
    path.append(a[r][c])
    next_r, next_c, next_value = -1, -1, -1
    for i in range(4):
        x, y = r + dx[i], c + dy[i]
        if not 1 <= x <= n or not 1 <= y <= n:
            continue
        if a[r][c] < a[x][y] and next_value == -1:
            next_r = x
            next_c = y
            next_value = a[x][y]
    if next_value != -1:
        r = next_r
        c = next_c
    else:
        break

print(*path)
