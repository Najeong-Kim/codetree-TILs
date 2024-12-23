import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = sys.maxsize

for i in range(min(arr), max(arr) + 1 - k):
    cost = 0
    start, end = i, i + k
    for elem in arr:
        if start <= elem <= end:
            continue
        if elem < start:
            cost += start - elem
        else:
            cost += elem - end
    result = min(result, cost)

print(result)
