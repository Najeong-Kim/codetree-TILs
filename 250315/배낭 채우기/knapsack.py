N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

arr = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = w[i - 1], v[i - 1]
    for j in range(M + 1):
        arr[i][j] = arr[i - 1][j]
        if j - W >= 0:
            arr[i][j] = max(arr[i][j], arr[i - 1][j - W] + V)

print(max(arr[-1]))
