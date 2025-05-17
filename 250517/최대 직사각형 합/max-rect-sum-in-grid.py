n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i - 1][j - 1]

result = - 10 ** 9
for a in range(1, n + 1):
    for b in range(1, n + 1):
        for i in range(a, n + 1):
            for j in range(b, n + 1):
                result = max(result, prefix_sum[i][j] - prefix_sum[i - a][j] - prefix_sum[i][j - b] + prefix_sum[i - a][j - b])

print(result)