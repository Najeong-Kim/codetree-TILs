import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

heap = []

for i in range(n):
    x, y = points[i]
    heapq.heappush(heap, (x + y, x, y))

for i in range(m):
    now = heapq.heappop(heap)
    heapq.heappush(heap, (now[0] + 4, now[1] + 2, now[2] + 2))

print(heap[0][1], heap[0][2])