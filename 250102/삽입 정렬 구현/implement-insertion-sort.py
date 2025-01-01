n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    temp = arr[i]
    now = i
    for j in reversed(range(1, i + 1)):
        if arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            now = j - 1
        else:
            break
    arr[now] = temp

for i in range(n):
    print(arr[i], end=" ")