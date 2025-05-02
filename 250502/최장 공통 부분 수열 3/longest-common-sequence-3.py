n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])

now = []
result = []
def find_result(i, j):
    global now
    global result
    
    if i == 0 and j == 0:
        now_arr = list(reversed(now))
        if not len(result):
            result = now_arr
        else:
            need_change = False
            for i in range(len(now_arr)):
                if now_arr[i] < result[i]:
                    need_change = True
                    break
            if need_change:
                result = now_arr
        return
    if i > 0 and j > 0 and dp[i - 1][j] != dp[i][j] and dp[i][j - 1] != dp[i][j] and dp[i - 1][j - 1] + 1 == dp[i][j]:
        now.append(a[i - 1])
        find_result(i - 1, j - 1)
        now.pop()
    else:
        if i > 0 and dp[i - 1][j] == dp[i][j]:
            find_result(i - 1, j)
        if j > 0 and dp[i][j - 1] == dp[i][j]:
            find_result(i, j - 1)
    
find_result(n, m)
print(*result)