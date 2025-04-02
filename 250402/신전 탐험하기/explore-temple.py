n = int(input())
arr = []
for i in range(n):
    left, mid, right = map(int, input().split())
    arr.append([left, mid, right])

dp = [[0] * 3 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    for j in range(3):
        dp[i][j] = max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + arr[i][j]

print(max(dp[-1]))