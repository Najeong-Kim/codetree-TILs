n = int(input())
sequence = list(map(int, input().split()))

arr = [[1, 1] for _ in range(n)]

for i in range(n):
    now = sequence[i]
    for j in range(i + 1, n):
        if now < sequence[j]:
            arr[j][0] = max(arr[j][0], arr[i][0] + 1)

for i in range(n):
    now = sequence[-i-1]
    for j in range(i + 1, n):
        if now < sequence[-j-1]:
            arr[-j-1][1] = max(arr[-j-1][1], arr[-i-1][1] + 1)

result = 0
for i in range(n):
    result = max(result, sum(arr[i]) - 1)

print(result)
