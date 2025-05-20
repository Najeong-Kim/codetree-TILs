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
            if arr[i] > heap1[0]:
                heapq.heappush(heap1, arr[i])
                heapq.heappush(heap2, -heapq.heappop(heap1))
            else:
                heapq.heappush(heap2, -arr[i])
            continue
        if i % 2 == 0:
            if arr[i] > -heap2[0]:
                heapq.heappush(heap1, arr[i])
            else:
                heapq.heappush(heap1, -heapq.heappop(heap2))
                heapq.heappush(heap2, -arr[i])
            print(heap1[0], end=' ')
        else:
            if arr[i] > heap1[0]:
                heapq.heappush(heap2, -heapq.heappop(heap1))
                heapq.heappush(heap2, -arr[i])
            else:
                heapq.heappush(heap2, -arr[i])
    print()
