N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]
missing.sort()
current = 0
arr = [0]
for i in range(1, N + 1):
    if current < B and missing[current] == i:
        arr.append(arr[-1] + 1)
        current += 1
    else:
        arr.append(arr[-1])

result = 10 ** 9
for i in range(N - K + 1):
    result = min(result, arr[i + K] - arr[i])

print(result)