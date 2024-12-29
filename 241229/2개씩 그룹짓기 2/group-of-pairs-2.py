import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = sys.maxsize

for i in range(n):
    result = min(result, arr[i + n] - arr[i])

print(result)