import math

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
# dp = [[-math.inf, 0] for _ in range(n + 1)]
dp = [-math.inf] * (n + 1)
dp[0] = [0, 0]


for i in range(n):
    if numbers[i] < 0:

    dp[i + 1] = 