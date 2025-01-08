n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = -1

for i in range(n):
    for j in range(i + 1, n + 1):
        for k in range(m):
            for l in range(k + 1, m + 1):
                is_positive = True
                for a in range(i, j):
                    for b in range(k, l):
                        if grid[a][b] <= 0:
                            is_positive = False
                if is_positive:
                    result = max(result, (j - i) * (l - k))

print(result)