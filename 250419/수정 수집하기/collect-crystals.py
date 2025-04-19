import math

n, k = map(int, input().split())
str = input()

dp = [[[-math.inf, -math.inf] for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(1, n + 1):
    if str[i - 1] == 'L':
        for j in range(k + 1):
            if j > 0:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1] + 1)
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0])
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0] + 1)
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1])
    else:
        for j in range(k + 1):
            if j > 0:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0] + 1)
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1])
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1] + 1)
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0])

result = 0
for i in range(n + 1):
    for j in range(k + 1):
        result = max(result, max(dp[i][j]))

print(result)