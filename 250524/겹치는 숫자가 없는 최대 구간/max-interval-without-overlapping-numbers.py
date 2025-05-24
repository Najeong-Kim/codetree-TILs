n = int(input())
arr = list(map(int, input().split()))

j = 0
result = 1
count = [False] * (10 ** 5 + 1)
count[arr[0]] = True

for i in range(n):
    while j + 1 < n:
        next = arr[j + 1]
        if not count[next]:
            count[next] = True
            j += 1
            result = max(result, j - i + 1)
        else:
            count[arr[i]] = False
            break

print(result)