from sortedcontainers import SortedSet
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

s = SortedSet(points)

# Please write your code here.
for query in queries:
    index = s.bisect_left(query)
    if index == len(s):
        print(-1, -1)
    else:
        print(s[index][0], s[index][1])
