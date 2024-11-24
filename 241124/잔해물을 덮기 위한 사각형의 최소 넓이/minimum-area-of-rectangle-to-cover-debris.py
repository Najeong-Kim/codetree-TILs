arr = [[0 for col in range(2000)] for row in range(2000)]

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    number = 1 if i == 0 else 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arr[i + 1000][j + 1000] = number

min_x, min_y, max_x, max_y = 2000, 2000, 0, 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            min_x, max_x = min(min_x, i), max(max_x, i)
            min_y, max_y = min(min_y, j), max(max_y, j)

result = (max_x - min_x) * (max_y - min_y)

print(result)
