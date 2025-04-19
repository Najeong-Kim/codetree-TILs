n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + a[i - 1][j])

print(max(dp[-1]))