n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort(key=lambda x: x[1])

dp = [0] * n
dp[0] = jobs[0][2]
for i in range(1, n):
    last = 0
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            last = max(last, dp[j])
    dp[i] = max(dp[i - 1], last + jobs[i][2])

print(dp[-1])
