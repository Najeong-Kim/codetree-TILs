import math
N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

arr = [[False] * N for _ in range(M)]

for j in range(N):
    for k in range(clothes[j][0] - 1, clothes[j][1]):
        arr[k][j] = True

dp = [[-math.inf] * N for _ in range(M)]

for i in range(N):
    dp[0][i] = 0

for i in range(1, M):
    for j in range(N):
        if not arr[i][j]:
            continue
        for k in range(N):
            if arr[i - 1][k]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[k] - v[j]))

print(max(dp[-1]))