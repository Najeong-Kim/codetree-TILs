n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * (n - m + 1) for _ in range(n)]

def check_sum(x, y):
    now = weight[x][y:y + m]
    result = 0
    check = 0

    def pick_stone(index, count):
        nonlocal result
        nonlocal check
        if index >= m:
            result = max(result, check)
            return
        
        pick_stone(index + 1, count)

        if now[index] + count <= c:
            count += now[index]
            check += now[index] ** 2
            pick_stone(index + 1, count)
            count -= now[index]
            check -= now[index] ** 2

    pick_stone(0, 0)
    return result

for i in range(n):
    for j in range(n - m + 1):
        arr[i][j] = check_sum(i, j)

result = 0
for i in range(n):
    for j in range(n - m + 1):
        for a in range(n):
            for b in range(n - m + 1):
                if i == a and abs(b - j) < m:
                    continue
                result = max(result, arr[i][j] + arr[a][b])

print(result)