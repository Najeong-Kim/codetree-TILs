n, q = map(int, input().split())
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]

arr = [0] * (max(points) + 1)

for point in points:
    arr[point] += 1

prefix_sum = [0]
for i in range(1, len(arr)):
    prefix_sum.append(prefix_sum[-1] + arr[i])

for r in ranges:
    start, end = r
    print(prefix_sum[min(end, len(prefix_sum) - 1)] - prefix_sum[start - 1])
