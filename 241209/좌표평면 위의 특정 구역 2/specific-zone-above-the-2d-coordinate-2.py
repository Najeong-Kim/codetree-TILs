N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 40000*40000

for i in range(N):
    x_min, x_max = 40001, 0
    y_min, y_max = 40001, 0
    for idx, elem in enumerate(arr):
        if idx == i:
            continue
        x_min, x_max = min(x_min, elem[0]), max(x_max, elem[0])
        y_min, y_max = min(y_min, elem[1]), max(y_max, elem[1])
    result = min(result, (x_max - x_min) * (y_max - y_min))

print(result)