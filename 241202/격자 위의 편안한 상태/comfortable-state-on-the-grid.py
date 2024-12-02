N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

for i in range(M):
    r, c = map(int, input().split())
    arr[r][c] = 1
    count = 0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if in_range(nx, ny) and arr[nx][ny] == 1:
            count += 1
    if count == 3:
        print(1)
    else:
        print(0)