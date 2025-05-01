import math
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [[math.inf] * (M) for _ in range(N - 1)]
for i in range(N - 1):
    dp[i][0] = 0

for i in range(1, N - 1):
    for j in range(1, M):
        dp[i][j] = min(dp[i - 1][j], dp[i - 2][j - 1] + numbers[i])

print(sum(numbers) - dp[-1][-1])