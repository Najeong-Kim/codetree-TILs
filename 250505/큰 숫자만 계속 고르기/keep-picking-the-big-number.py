import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heap = []

for i in range(n):
    heapq.heappush(heap, -arr[i])

for i in range(m):
    heapq.heappush(heap, heapq.heappop(heap) + 1)

print(-heapq.heappop(heap))