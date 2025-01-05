n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

dx1 = [1,-1,1,-1,-1,0]
dy1 = [0,0,0,0,0,-1]
dx2 = [0,0,0,0,1,0]
dy2 = [1,1,-1,-1,0,1]

for i in range(n):
    for j in range(m):
        for k in range(6):
            x1, y1 = i + dx1[k], j + dy1[k]
            x2, y2 = i + dx2[k], j + dy2[k]
            if x1 < 0 or x1 >= n or x2 < 0 or x2 >= n or y1 < 0 or y1 >= m or y2 < 0 or y2 >= m:
                continue
            result = max(result, grid[i][j] + grid[x1][y1] + grid[x2][y2])

print(result)
