n = int(input())
arr = list(map(int, input().split()))
is_sorted = True

for i in range(n):
    is_sorted = True
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            is_sorted = False
    if is_sorted:
        break

for i in range(n):
    print(arr[i], end=" ")