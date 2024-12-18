N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

result = [0] * 1000001

for i in range(1, 1000001):
    if not i in arr:
        continue
    count = 0
    for j in range(N):
        check = arr[max(0, j - K):min(N, j + K + 1)]
        if i == arr[j] and check.count(i) >= 2:
            count += 1
    result[i] = count

print(result.index(max(result)))
