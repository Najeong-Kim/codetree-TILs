N = int(input())
arr = [[0 for col in range(200)] for row in range(200)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

result = 0
for i in arr:
    for j in i:
        if j == 1:
            result += 1

print(result)
