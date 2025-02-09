n = int(input())
m = list(map(int, input().split()))
arr = [1] * n

for i in range(n):
    now = m[i]
    for j in range(1, min(now + 1, n)):
        if now < m[j]:
            arr[j] = max(arr[j], arr[i] + 1)

print(max(arr))
