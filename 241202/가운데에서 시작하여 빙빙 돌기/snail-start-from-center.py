n = int(input())
answer = [
    [0] * n
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = n - 1, n - 1
dir_num = 2

answer[x][y] = n * n

for i in range(1, n * n):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = (n * n) - i

# Output:
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()
