n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
prefix_sum = {
    'a': [[0] * (m + 1) for _ in range(n + 1)],
    'b': [[0] * (m + 1) for _ in range(n + 1)],
    'c': [[0] * (m + 1) for _ in range(n + 1)]
}

words = 'abc'

for i in range(n):
    for j in range(m):
        for l in range(3):
            if grid[i][j] == words[l]:
                prefix_sum[words[l]][i + 1][j + 1] = prefix_sum[words[l]][i + 1][j] + prefix_sum[words[l]][i][j + 1] - prefix_sum[words[l]][i][j] + 1
            else:
                prefix_sum[words[l]][i + 1][j + 1] = prefix_sum[words[l]][i + 1][j] + prefix_sum[words[l]][i][j + 1] - prefix_sum[words[l]][i][j]

for i in range(k):
    r1, c1, r2, c2 = queries[i]
    for j in range(3):
        print(prefix_sum[words[j]][r2][c2] - prefix_sum[words[j]][r2][c1 - 1] - prefix_sum[words[j]][r1 - 1][c2] + prefix_sum[words[j]][r1 - 1][c1 - 1], end=' ')
    print()