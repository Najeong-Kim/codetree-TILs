n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 10 ** 9

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for k in range(1, 101):
    arr = [[10 ** 9] * n for _ in range(n)]
    arr[0][0] = grid[0][0]
    
    for i in range(n):
        for j in range(n):
            if i > 0 and grid[i][j] >= k:
                arr[i][j] = min(max(arr[i - 1][j], grid[i][j]), arr[i][j])
            if j > 0 and grid[i][j] >= k:
                arr[i][j] = min(max(arr[i][j - 1], grid[i][j]), arr[i][j])
    result = min(result, arr[n - 1][n - 1] - k)

print(result)