n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

dp = [[0] * (n + 1) for _ in range(2 * n)]
dp[0][0] = red[0]
dp[0][1] = blue[0]

for i in range(1, 2 * n):
    for j in range(n + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + blue[i])
        if i - j < n:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + red[i])

print(max(dp[-1]))