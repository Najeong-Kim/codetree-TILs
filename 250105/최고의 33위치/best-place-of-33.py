n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n - 2):
    for j in range(n - 2):
        coins = sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3])
        result = max(result, coins)

print(result)
