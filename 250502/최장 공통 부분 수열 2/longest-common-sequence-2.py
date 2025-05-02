A = input()
B = input()

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])

result = ''
is_print = False

def find_result(i, j):
    global result
    global is_print
    if is_print:
        return

    if i == 0 and j == 0:
        is_print = True
        print(result[::-1])
        return

    if dp[i - 1][j - 1] + 1 == dp[i][j]:
        result += A[i - 1]
        find_result(i - 1, j - 1)
        result = result[:-1]
    else:
        if i > 0 and dp[i - 1][j] == dp[i][j]:
            find_result(i - 1, j)
        if j > 0 and dp[i][j - 1] == dp[i][j]:
            find_result(i, j - 1)

find_result(len(A), len(B))
