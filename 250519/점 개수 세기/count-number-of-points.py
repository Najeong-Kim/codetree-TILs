import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

points.sort()

for i in range(q):
    a, b = queries[i]
    print(bisect_right(points, b) - bisect_left(points, a))
    