n, m = map(int, input().split())
A = list(map(int, input().split()))
arr = [10 ** 9] * (m + 1)
arr[0] = 0

for elem in A:
    for i in range(m):
        index = m - i
        now = index - elem
        if now < 0:
            continue
        arr[index] = min(arr[index], arr[now] + 1)

if arr[m] == 10 ** 9:
    print(-1)
else:
    print(arr[m])
