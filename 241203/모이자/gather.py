import sys

n = int(input())
arr = list(map(int, input().split()))

INF_MAX = sys.maxsize

min_range = INF_MAX

for i in range(n):
    sum = 0
    for j, elem in enumerate(arr):
        sum += abs(j - i) * elem
    min_range = min(min_range, sum)

print(min_range)