import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

heap = []

for i in range(n):
    if x[i] == 0:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x[i])