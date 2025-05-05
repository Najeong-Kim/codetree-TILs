import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []

for i in range(n):
    heapq.heappush(heap, -arr[i])

while len(heap) > 1:
    first = -heapq.heappop(heap)
    second = -heapq.heappop(heap)
    if first == second:
        continue
    heapq.heappush(heap, -(first - second))

if len(heap):
    print(-heap[0])
else:
    print(-1)
