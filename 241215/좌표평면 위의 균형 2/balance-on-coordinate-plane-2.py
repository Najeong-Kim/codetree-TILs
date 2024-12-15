import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = sys.maxsize

for i in range(0, 100, 2):
    for j in range(0, 100, 2):
        a, b, c, d = 0, 0, 0, 0
        for elem in arr:
            if elem[0] > i and elem[1] > j:
                a += 1
            elif elem[0] < i and elem[1] > j:
                b += 1
            elif elem[0] > i and elem[1] < j:
                c += 1
            else:
                d += 1
        result = min(result, max(a, b, c, d))

print(result)