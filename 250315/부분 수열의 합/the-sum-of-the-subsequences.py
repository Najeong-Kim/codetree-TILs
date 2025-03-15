n, m = map(int, input().split())
A = list(map(int, input().split()))
arr = [False] * (m + 1)

arr[0] = True

for elem in A:
    for i in range(m):
        index = m - i
        now = index - elem
        if now < 0 or not arr[now]:
            continue
        arr[index] = True

if arr[m]:
    print('Yes')
else:
    print('No')