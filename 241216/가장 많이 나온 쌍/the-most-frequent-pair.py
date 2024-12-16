n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

result = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        count = 0
        for k in arr:
            if min(k) == i and max(k) == j:
                count += 1
        result = max(result, count)

print(result)
