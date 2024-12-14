n = int(input())
arr = list(map(int, input().split()))

result = 0

for i in range(1, 100):
    count = 0
    for j in range(n):
        for k in range(j + 1, n):
            a, b = arr[j], arr[k]
            if a - i == i - b:
                count += 1
    result = max(result, count)

print(result)