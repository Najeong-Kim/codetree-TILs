n = int(input())
arr = [[0 for col in range(201)] for row in range(201)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    color = 'r' if i % 2 == 0 else 'b'
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = color

result = 0
for i in arr:
    for j in i:
        if j == 'b':
            result += 1

print(result)
