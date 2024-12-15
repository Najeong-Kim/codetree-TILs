import sys

n = int(input())
arr = list(map(int, input().split()))

result = sys.maxsize

for i in range(n):
    sub = arr[:]
    sub[i] = arr[i] * 2
    for j in range(n):
        if i == j:
            continue
        now = sub[:]
        del now[j]
        differences = 0
        for k in range(len(now) - 1):
            differences += abs(now[k] - now[k + 1])
        result = min(result, differences)

print(result)
