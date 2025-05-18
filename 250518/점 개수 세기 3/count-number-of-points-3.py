from sortedcontainers import SortedSet

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
s = SortedSet()
for point in points:
    s.add(point)

mapper = dict()
cnt = 1
for num in s:
    mapper[num] = cnt
    cnt += 1

for query in queries:
    print(mapper[query[1]] - mapper[query[0]] + 1)