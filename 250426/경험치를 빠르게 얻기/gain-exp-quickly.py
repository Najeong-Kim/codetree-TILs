import math

n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    exp, time = quests[i]
    for j in range(m, -1, -1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        next_exp = min(j + exp, m)
        dp[i + 1][next_exp] = min(dp[i + 1][next_exp], dp[i][j] + time, dp[i][next_exp])

print(dp[-1][-1])