n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    now = i + 1
    for j in range(now, n):
        if arr[now] > arr[j]:
            now = j
    if arr[i] > arr[now]:
        temp = arr[i]
        arr[i] = arr[now]
        arr[now] = temp

for i in range(n):
    print(arr[i], end=" ")