n, m = map(int, input().split())
arr = list(map(int, input().split()))
wifi = [False] * n

count = 0

for i in range(len(arr)):
    if arr[i] == 1 and not wifi[i]:
        for j in range(i, min(len(wifi), i + (2 * m) + 1)):
            wifi[j] = True
        count += 1

print(count)