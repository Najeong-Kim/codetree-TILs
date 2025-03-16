N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

arr = [0] * (M + 1)

for i in range(1, M + 1):
    for j in range(N):
        W, V = w[j], v[j]
        if i - W >= 0:
            arr[i] = max(arr[i], arr[i - W] + V)

print(arr[-1])
