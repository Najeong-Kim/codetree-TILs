n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

dp = [[[-1] * 10 for _ in range(12)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    for j in range(12):
        for k in range(10):
            if dp[i][j][k] == -1:
                continue
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
            if j + 1 <= 11:
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + s[i])
            if k + 1 <= 9:
                dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + b[i])

print(dp[-1][-1][-1])