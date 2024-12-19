import sys
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = sys.maxsize

dividers = list(combinations([i + 1 for i in range(n - 1)], m - 1))

for divider in dividers:
    count = 0
    for i, elem in enumerate(divider):
        if i == 0:
            count = max(count, sum(arr[:elem]))
        else:
            count = max(count, sum(arr[divider[i - 1]:elem]))
    count = max(count, sum(arr[divider[-1]:]))
    result = min(result, count)

print(result)