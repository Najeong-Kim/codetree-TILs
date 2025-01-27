n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# Write your code here!
for _ in range(t):
    board = [[0] * n for _ in range(n)]
    for marble in marbles:
        index, value = -1, 0
        x, y = marble[0] - 1, marble[1] - 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny):
                continue
            if a[nx][ny] > value:
                index = i
                value = a[nx][ny]
        board[x + dx[index]][y + dy[index]] += 1
    now = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                now.append((i + 1, j + 1))
    marbles = now

print(len(marbles))
