import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []
heapq.heappush(heap, arr[-1])

result = 0
for i in range(1, n):
    heapq.heappush(heap, arr[-1-i])
    result = max(result, sum(heap[1:]) / (len(heap) - 1))

print("{:0.2f}".format(result))
