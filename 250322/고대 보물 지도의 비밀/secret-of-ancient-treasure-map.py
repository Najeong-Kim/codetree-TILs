import math

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [[-math.inf] * (k + 1) for _ in range(n)]
if numbers[0] < 0:
    dp[0][0] = 0
    dp[0][1] = numbers[0]
else:
    dp[0][0] = numbers[0]

for i in range(1, n):
    if numbers[i] < 0:
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + numbers[i]
    else:
        dp[i][0] = max(dp[i - 1][0], numbers[i])
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + numbers[i]

result = -math.inf
for elem in dp:
    result = max(result, max(elem))

print(result)