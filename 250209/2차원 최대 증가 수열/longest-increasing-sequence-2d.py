n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * m for _ in range(n)]
arr[0][0] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            continue
        for a in range(i + 1, n):
            for b in range(j + 1, m):
                if grid[a][b] > grid[i][j]:
                    arr[a][b] = max(arr[a][b], arr[i][j] + 1)

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, arr[i][j])

print(result)