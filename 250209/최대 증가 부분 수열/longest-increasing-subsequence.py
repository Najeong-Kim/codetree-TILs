n = int(input())
m = list(map(int, input().split()))
arr = [1] * n

for i in range(n):
    now = m[i]
    for j in range(i + 1, min(i + 1 + now, n)):
        if now < m[j]:
            arr[j] = max(arr[j], arr[i] + 1)

print(max(arr))
