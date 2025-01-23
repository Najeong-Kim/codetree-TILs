n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

is_blocked = False
# Write your code here!
for i in range(n):
    for j in range(k - 1, k + m - 1):
        if grid[i][j] == 1:
            is_blocked = True
            break
    if is_blocked:
        for j in range(k - 1, k + m - 1):
            grid[i - 1][j] = 1
        break

if not is_blocked:
    for j in range(k - 1, k + m - 1):
        grid[n - 1][j] = 1
    
for elem in grid:
    print(*elem)