N, M = map(int, input().split())
coin = list(map(int, input().split()))
arr = [-1] * (M + 1)
arr[0] = 0

for i in range(1, M + 1):
    for j in range(N):
        now = i - coin[j]
        if now < 0 or arr[now] == -1:
            continue
        arr[i] = max(arr[i], arr[now] + 1)

print(arr[M])
