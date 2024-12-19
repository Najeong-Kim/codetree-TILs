import sys

N = int(input())
arr = [int(input()) for _ in range(N)]

if max(arr) - min(arr) <= 17:
    print(0)
    exit()

result = sys.maxsize

for i in range(min(arr), max(arr) - 16):
    start, end = i, i + 17
    count = 0
    for elem in arr:
        if start > elem:
            count += (start - elem) ** 2
        elif end < elem:
            count += (elem - end) ** 2
    result = min(count, result)

print(result)
