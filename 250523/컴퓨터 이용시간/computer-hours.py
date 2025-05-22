import heapq

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
p = [interval[0] for interval in intervals]
q = [interval[1] for interval in intervals]

arr = []

for i in range(n):
    arr.append((p[i], 1, i))
    arr.append((q[i], -1, i))

arr.sort()
heap = [i for i in range(1, n + 1)]
heapq.heapify(heap)
seated = [0] * n

for i in range(len(arr)):
    time, value, index = arr[i]
    if value == 1:
        seated[index] = heapq.heappop(heap)
    else:
        heapq.heappush(heap, seated[index])

print(*seated)