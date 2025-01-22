import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

result = 0

# Write your code here!
for i in range(n):
    for j in range(n):
        copied_grid = copy.deepcopy(grid)
        value = grid[i][j]
        for k in range(value):
            for l in range(4):
                x, y = i + dx[l] * k, j + dy[l] * k
                if 0 <= x < n and 0 <= y < n:
                    copied_grid[x][y] = 0
        arr = [[] for _ in range(n)]
        for k in range(n):
            now = []
            for l in reversed(range(n)):
                if copied_grid[l][k] != 0:
                    now.append(copied_grid[l][k])
            while len(now) < n:
                now.append(0)
            now.reverse()
            for l in range(n):
                arr[l].append(now[l])
        copied_grid = arr
        
        count = 0
        for k in range(n):
            for l in range(n):
                if copied_grid[k][l] == 0:
                    continue
                if k < n - 1 and copied_grid[k][l] == copied_grid[k + 1][l]:
                    count += 1
                if l < n - 1 and copied_grid[k][l] == copied_grid[k][l + 1]:
                    count += 1
        result = max(result, count)

print(result)