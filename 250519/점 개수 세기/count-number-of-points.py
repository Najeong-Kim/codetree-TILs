from sortedcontainers import SortedSet
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

s = SortedSet(points)

for i in range(q):
    a, b = queries[i]
    print(s.bisect_right(b) - s.bisect_left(a))
    