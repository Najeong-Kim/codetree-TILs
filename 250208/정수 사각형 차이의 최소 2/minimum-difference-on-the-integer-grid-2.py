n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [[[10 ** 9, 0] for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

arr[0][0] = [grid[0][0], grid[0][0]]

for i in range(n):
    for j in range(n):
        first = arr[i][j]
        second = arr[i][j]

        if i > 0:
            first = [min(arr[i - 1][j][0], arr[i][j][0], grid[i][j]), max(arr[i - 1][j][1], arr[i][j][1], grid[i][j])]
        if j > 0:
            second = [min(arr[i][j - 1][0], arr[i][j][0], grid[i][j]), max(arr[i][j - 1][1], arr[i][j][1], grid[i][j])]
        if first[1] == 0 or abs(first[1] - first[0]) > abs(second[1] - second[0]):
            arr[i][j] = second
        else:
            arr[i][j] = first

print(arr[n - 1][n - 1][1] - arr[n - 1][n - 1][0])