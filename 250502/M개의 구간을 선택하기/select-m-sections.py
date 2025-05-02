import math
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [[[-math.inf, -math.inf] for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(M + 1):
        dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][0], dp[i][j][1])
        dp[i + 1][j][1] = max(dp[i + 1][j][1], dp[i][j][1] + numbers[i])
        if j < M:
            dp[i + 1][j + 1][1] = max(dp[i + 1][j + 1][1], dp[i][j][0] + numbers[i])

print(max(dp[-1][-1]))
