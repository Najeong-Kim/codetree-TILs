n = int(input())

dp = [[[0] * 3 for _ in range(3)] for _ in range(n)]
dp[0][0][0] = 1
dp[0][0][1] = 1
dp[0][1][0] = 1

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            dp[i][j][0] += dp[i - 1][j][k]
    for j in range(1, 3):
        for k in range(3):
            dp[i][j][0] += dp[i - 1][j - 1][k]
    for j in range(3):
        for k in range(1, 3):
            dp[i][j][k] += dp[i - 1][j][k - 1]

result = 0
for elem in dp[-1]:
    result += sum(elem)
print(result % (10 ** 9 + 7))