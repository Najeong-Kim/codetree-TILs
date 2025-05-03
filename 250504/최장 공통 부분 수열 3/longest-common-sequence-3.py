import sys
sys.setrecursionlimit(100000)
from functools import lru_cache

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        x = n - 1 - i
        y = m - 1 - j
        if a[x] == b[y]:
            dp[x][y] = dp[x + 1][y + 1] + 1
        else:
            dp[x][y] = max(dp[x + 1][y], dp[x][y + 1])

@lru_cache(None)
def find_result(i, j):
    if i == n or j == m:
        return []
    result = []
    for x in range(i, n):
        for y in range(j, m):
            if a[x] == b[y] and dp[x][y] == dp[i][j]:
                candidate = [a[x]] + find_result(x + 1, y + 1)
                if not len(result):
                    result = candidate
                    continue
                need_change = True
                for k in range(len(candidate)):
                    if candidate[k] < result[k]:
                        break
                    if candidate[k] > result[k]:
                        need_change = False
                        break
                if need_change:
                    result = candidate
    return result

print(*find_result(0, 0))
