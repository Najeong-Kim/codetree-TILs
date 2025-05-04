from sortedcontainers import SortedSet

n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.
s = SortedSet()
for point in points:
    s.add(point)

for query in queries:
    index = s.bisect_left((query, 0))

    if index == len(s):
        print(-1, -1)
    else:
        value = s[index]
        print(s[index][0], s[index][1])
        s.remove(value)