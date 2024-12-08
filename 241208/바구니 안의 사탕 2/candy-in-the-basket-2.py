N, K = map(int, input().split())
arr = [0] * 101

for _ in range(N):
    candies, coordinate = map(int, input().split())
    arr[coordinate] += candies

result = 0

if K >= 50:
    result = sum(arr)

for i in range(K, len(arr) - K):
    result = max(result, sum(arr[i-K:i+K+1]))

print(result)
