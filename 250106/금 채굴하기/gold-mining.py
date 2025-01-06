n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

for i in range(n):
    for j in range(n):
        arr = []
        for k in range(n + 1):
            for l in range(k + 1):
                check = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 2), (0, 3), (1, 2), (1, 3)]
                for a in check:
                    x = i + dx[a[0]] * l + dx[a[1]] * (k - l)
                    y = j + dy[a[0]] * l + dy[a[1]] * (k - l)
                    if 0 <= x < n and 0 <= y < n and (x, y) not in arr:
                        arr.append((x, y))
            count = 0
            for elem in arr:
                if grid[elem[0]][elem[1]] == 1:
                    count += 1
            if (k * k + (k + 1) * (k + 1)) <= count * m:
                result = max(result, count)

print(result)