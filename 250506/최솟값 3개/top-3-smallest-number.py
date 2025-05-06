import heapq

n = int(input())
arr = list(map(int, input().split()))

heap = []

for i in range(n):
    heapq.heappush(heap, arr[i])
    if len(heap) < 3:
        print(-1)
    else:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        three = heapq.heappop(heap)
        print(one * two * three)
        heapq.heappush(heap, one)
        heapq.heappush(heap, two)
        heapq.heappush(heap, three)
