n = int(input())
m = list(map(int, input().split()))
arr = [1] * n

for i in range(n):
    for j in range(i + 1, n):
        if m[i] > m[j]:
            arr[j] = max(arr[j], arr[i] + 1)

print(max(arr))