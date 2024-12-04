import sys

N = int(input())
arr = [int(input()) for _ in range(N)]

min_result = sys.maxsize

for i in range(N):
    result = 0
    for j in range(N):
        result += ((j - i + N) % N) * arr[j]
    min_result = min(min_result, result)

print(min_result)