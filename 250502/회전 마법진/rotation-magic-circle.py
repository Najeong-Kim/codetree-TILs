import math

N = int(input())
a = input()
b = input()

dp = [[math.inf] * 10 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(10):
        if dp[i][j] == math.inf:
            continue
        now = int(a[i]) + (j % 10)
        target = int(b[i])
        clockwise = (10 + now - target) % 10
        counterclockwise = (10 + target - now) % 10
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + clockwise)
        dp[i + 1][(j + counterclockwise) % 10] = min(dp[i + 1][(j + counterclockwise) % 10], dp[i][j] + counterclockwise)

print(min(dp[-1]))
    