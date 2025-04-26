import math

n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

dp = [math.inf] * (m + 1)
dp[0] = 0

for i in range(n):
    exp, time = quests[i]
    for j in range(m, -1, -1):
        next_exp = min(j + exp, m)
        dp[next_exp] = min(dp[next_exp], dp[j] + time)

if dp[-1] == math.inf:
    print(-1)
else:
    print(dp[-1])