N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = [[0] * 41 for _ in range(N)]
dp[0][20 + nums[0]] += 1
dp[0][20 - nums[0]] += 1

for i in range(1, N):
    for j in range(41):
        if j - nums[i] >= 0:
            dp[i][j - nums[i]] += dp[i - 1][j]
        if j + nums[i] <= 40:
            dp[i][j + nums[i]] += dp[i - 1][j]

print(dp[-1][M + 20])
