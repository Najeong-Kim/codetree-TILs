N = int(input())
arr = [[0 for col in range(200)] for row in range(200)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i + 100][j + 100] = 1

result = 0
for i in arr:
    for j in i:
        if j == 1:
            result += 1

print(result)
