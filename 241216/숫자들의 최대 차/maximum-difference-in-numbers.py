N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

result = 0

for i in range(N):
    for j in range(i + 1, N):
        cur = arr[i:j]
        if (max(cur) - min(cur)) <= K:
            result = max(result, len(cur))

print(result)
