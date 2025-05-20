import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    heap1 = []
    heap2 = []
    for i in range(m):
        if i == 0:
            heapq.heappush(heap1, arr[i])
            print(heap1[0], end=' ')
            continue
        if i == 1:
            heapq.heappush(heap1, arr[i])
            heapq.heappush(heap2, -heapq.heappop(heap1))
            continue
        if i % 2 == 0:
            heapq.heappush(heap2, -arr[i])
            heapq.heappush(heap1, -heapq.heappop(heap2))
            print(heap1[0], end=' ')
        else:
            heapq.heappush(heap1, arr[i])
            heapq.heappush(heap2, -heapq.heappop(heap1))
    print()
