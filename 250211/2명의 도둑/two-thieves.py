n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * (n - m + 1) for _ in range(n)]

def check_sum(x, y):
    now = weight[x][y:y + m]
    now.sort()
    result = 0
    count = 0
    for elem in reversed(now):
        if count + elem <= c:
            count += elem
            result += elem ** 2
    return result

for i in range(n):
    for j in range(n - m + 1):
        arr[i][j] = check_sum(i, j)

result = 0
for i in range(n):
    for j in range(n - m + 1):
        for a in range(n):
            for b in range(j, n - m + 1):
                if i == a and b - j < m:
                    continue
                result = max(result, arr[i][j] + arr[a][b])

print(result)