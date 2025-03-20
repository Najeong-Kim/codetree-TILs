n = int(input())
coin = [0] + list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n + 1)]
dp[1][1] = coin[1]

for i in range(2, n + 1):
    dp[i][0] = dp[i - 2][0] + coin[i]
    dp[i][1] = max(dp[i - 2][1] + coin[i], dp[i - 1][0] + coin[i])
    dp[i][2] = max(dp[i - 2][2] + coin[i], dp[i - 1][1] + coin[i])
    dp[i][3] = max(dp[i - 2][3] + coin[i], dp[i - 1][2] + coin[i])


print(max(dp[n]))