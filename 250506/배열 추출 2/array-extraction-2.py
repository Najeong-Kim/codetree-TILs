import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

heap = []

for i in range(n):
    if x[i] != 0:
        heapq.heappush(heap, (abs(x[i]), x[i]))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
