import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []
heapq.heappush(heap, arr[-1])

result = 0
total = heap[0]
for i in range(1, n):
    now = arr[-1-i]
    heapq.heappush(heap, now)
    total += now
    result = max(result, (total - heap[0]) / i)

print("{:0.2f}".format(result))
