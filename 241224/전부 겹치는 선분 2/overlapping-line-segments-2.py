n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [0] * 101

for elem in arr:
    x1, x2 = elem
    for j in range(x1, x2 + 1):
        check[j] += 1

if max(check) == n - 1:
    print('Yes')
else:
    print('No')