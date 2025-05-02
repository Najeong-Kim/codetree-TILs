import math

N = int(input())
a = input()
b = input()

dp = [math.inf] * (9 * N + 10)
dp[0] = 0

active = {0}

for i in range(N):
    now_dp = [math.inf] * (9 * N + 10)
    now_active = set()
    for j in active:
        if dp[j] == math.inf:
            continue
        now = int(a[i]) + (j % 10)
        target = int(b[i])
        clockwise = (10 + now - target) % 10
        counterclockwise = (10 + target - now) % 10
        now_dp[j] = min(now_dp[j], dp[j] + clockwise)
        now_active.add(j)
        now_dp[j + counterclockwise] = min(now_dp[j + counterclockwise], dp[j] + counterclockwise)
        now_active.add(j + counterclockwise)
    dp = now_dp
    active = now_active

print(min(dp))
    