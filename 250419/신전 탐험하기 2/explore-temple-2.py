import math

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[[-math.inf, -math.inf, -math.inf] for _ in range(3)] for _ in range(n)]

for i in range(3):
    dp[0][i][i] = arr[0][i]

for i in range(1, n - 1):
    for j in range(3):
        for k in range(3):
            dp[i][j][k] = max(dp[i - 1][(j + 1) % 3][k], dp[i - 1][(j + 2) % 3][k]) + arr[i][j]

for j in range(3):
    for k in range(3):
        if j == k:
            continue
        i = n - 1
        dp[i][j][k] = max(dp[i - 1][(j + 1) % 3][k], dp[i - 1][(j + 2) % 3][k]) + arr[i][j]

result = 0
for i in range(3):
    result = max(result, max(dp[-1][i]))

print(result)
