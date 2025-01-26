n, m, r, c = map(int, input().split())
directions = list(input().split())
board = [[0] * n for _ in range(n)]
dice = [1, 6, 2, 5, 3, 4]
x, y = r - 1, c - 1
direcion_list, dx, dy = ['L', 'R', 'U', 'D'], [0, 0, -1, 1], [-1, 1, 0, 0]

def rotate_dice(index, arr):
    a, b, c, d, e, f = arr
    if direction == 'L':
        return [e, f, c, d, b, a]
    if direction == 'R':
        return [f, e, c, d, a, b]
    if direction == 'U':
        return [c, d, b, a, e, f]
    if direction == 'D':
        return [d, c, a, b, e, f]

board[x][y] = dice[1]

for direction in directions:
    index = direcion_list.index(direction)
    new_x, new_y = x + dx[index], y + dy[index]
    if not (0 <= new_x < n and 0 <= new_y < n):
        continue
    x, y = new_x, new_y
    dice = rotate_dice(direction, dice)
    board[x][y] = dice[1]

count = 0
for i in range(n):
    for j in range(n):
        count += board[i][j]

print(count)