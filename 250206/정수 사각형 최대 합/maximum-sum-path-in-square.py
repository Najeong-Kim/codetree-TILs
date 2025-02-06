n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

answer[0][0] = grid[0][0]

for i in range(1, n):
    answer[0][i] = answer[0][i - 1] + grid[0][i]
    answer[i][0] = answer[i - 1][0] + grid[i][0]

for i in range(1, n):
    for j in range(1, n):
        answer[i][j] = max(answer[i - 1][j] + grid[i][j], answer[i][j - 1] + grid[i][j])

print(answer[n - 1][n - 1])