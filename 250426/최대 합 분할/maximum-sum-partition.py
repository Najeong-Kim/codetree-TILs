n = int(input())
arr = list(map(int, input().split()))

limit = 10 ** 5 + 1

dp = [[-1] * (limit * 2 + 1) for _ in range(n + 1)]
dp[0][limit] = 0

for i in range(n):
    now = arr[i]
    for j in range(limit * 2 + 1):
        if dp[i][j] == -1:
            continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j - now >= 0:
            dp[i + 1][j - now] = max(dp[i + 1][j - now], dp[i][j] + now)
        if j + now < limit * 2:
            dp[i + 1][j + now] = max(dp[i + 1][j + now], dp[i][j] + now)

print(dp[-1][limit] // 2)
