import math

N, M = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[-math.inf] * 4 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0] = [0, 0, 0, 0]

for i in range(N):
    for j in range(M + 1):
        for k in range(4):
            if dp[i][j][k] == -math.inf:
                continue
            now = a[i]
            last = k + 1
            is_same = 1 if now == last else 0
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + is_same)
            if j < M:
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][(k + 1) % 4] + is_same)
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][(k + 2) % 4] + is_same)
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][(k + 3) % 4] + is_same)

print(max(dp[-1][-1]))