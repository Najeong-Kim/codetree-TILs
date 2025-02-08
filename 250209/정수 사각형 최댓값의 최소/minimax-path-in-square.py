n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [[10 ** 9] * n for _ in range(n)]

arr[0][0] = grid[0][0]

for i in range(n):
    for j in range(n):
        if i > 0:
            arr[i][j] = min(arr[i][j], max(arr[i - 1][j], grid[i][j]))
        if j > 0:
            arr[i][j] = min(arr[i][j], max(arr[i][j - 1], grid[i][j]))

print(arr[n - 1][n - 1])
