import sys

arr = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            first = arr[i] + arr[j] + arr[k]
            second = sum(arr) - first
            min_diff = min(min_diff, abs(first - second))

print(min_diff)