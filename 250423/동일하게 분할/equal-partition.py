n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
data = [[False] * (10 ** 5 + 1) for _ in range(n + 1)]
data[0][0] = True

for i in range(n):
    for j in range(10 ** 5 + 1):
        if data[i][j]:
            data[i + 1][j] = True
            if j + arr[i] <= 10 ** 5:
                data[i + 1][j + arr[i]] = True

if total % 2 == 0 and data[-1][total // 2]:
    print('Yes')
else:
    print('No')
