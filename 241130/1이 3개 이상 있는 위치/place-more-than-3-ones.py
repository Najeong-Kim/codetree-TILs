n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def is_more_three_adjacent_cells(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt >= 3

result = 0

for i in range(n):
    for j in range(n):
        if is_more_three_adjacent_cells(i, j):
            result += 1

print(result)