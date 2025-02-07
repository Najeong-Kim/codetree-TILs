n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = [[0] * n for _ in range(n)]

answer[0][0] = grid[0][0]

for i in range(n):
    for j in range(n):
        if i > 0:
            answer[i][j] = max(answer[i][j], min(answer[i - 1][j], grid[i][j]))
        if j > 0:
            answer[i][j] = max(answer[i][j], min(answer[i][j - 1], grid[i][j]))
        
print(answer[n - 1][n - 1])