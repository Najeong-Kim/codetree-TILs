n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * (n) for _ in range(n)]

answer[0][n - 1] = grid[0][n - 1]

for i in range(n):
    for j in reversed(range(n)):
        if i == 0 and j == n - 1:
            continue
        top = answer[i - 1][j] if i > 0 else 10 ** 9
        right = answer[i][j + 1] if j < n - 1 else 10 ** 9
        answer[i][j] = min(top + grid[i][j], right + grid[i][j])

print(answer[n - 1][0])
