n = int(input())
arr = list(map(int, input().split()))

j = 0
result = 1
count = [False] * (10 ** 5 + 1)
count[arr[0]] = True

for i in range(n):
    while j < n:
        now = arr[j]
        if not count[now]:
            count[now] = True
            j += 1
            result = max(result, j - i + 1)
        else:
            count[arr[i]] = False
            break

print(result)