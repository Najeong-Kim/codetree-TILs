import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

result = 0
for i in range(n - 1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    result += a + b
    heapq.heappush(arr, a + b)

print(result)