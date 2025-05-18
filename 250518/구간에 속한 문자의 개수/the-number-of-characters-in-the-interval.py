n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
prefix_sum = [[[0, 0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

words = 'abc'

for i in range(n):
    for j in range(m):
        for k in range(3):
            if grid[i][j] == words[k]:
                prefix_sum[i + 1][j + 1][k] = prefix_sum[i + 1][j][k] + prefix_sum[i][j + 1][k] - prefix_sum[i][j][k] + 1
            else:
                prefix_sum[i + 1][j + 1][k] = prefix_sum[i + 1][j][k] + prefix_sum[i][j + 1][k] - prefix_sum[i][j][k]

for i in range(k):
    r1, c1, r2, c2 = queries[i]
    for j in range(3):
        print(prefix_sum[r2][c2][j] - prefix_sum[r2][c1 - 1][j] - prefix_sum[r1 - 1][c2][j] + prefix_sum[r1 - 1][c1 - 1][j], end=' ')
    print()