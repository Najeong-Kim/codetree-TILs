n, m, r, c = map(int, input().split())
board = [[-1] * n for _ in range(n)]

board[r - 1][c - 1] = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for t in range(1, m + 1):
    distance = 2 ** (t - 1)
    for i in range(n):
        for j in range(n):
            if 0 <= board[i][j] < t:
                for k in range(4):
                    new_x, new_y = i + dx[k] * distance, j + dy[k] * distance
                    if in_range(new_x, new_y) and board[new_x][new_y] == -1:
                        board[new_x][new_y] = t

count = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != -1:
            count += 1

print(count)
