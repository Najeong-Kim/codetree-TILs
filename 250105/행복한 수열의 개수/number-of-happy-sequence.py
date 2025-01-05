n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

def is_happy(arr):
    now = None
    count = 0
    for elem in arr:
        if now == elem:
            count += 1
        else:
            now = elem
            count = 1
        if count == m:
            return True
    return False

for i in range(n):
    arr = grid[i]
    if is_happy(arr):
        result += 1

for j in range(n):
    arr = []
    for k in range(n):
        arr.append(grid[k][j])
    if is_happy(arr):
        result += 1

print(result)