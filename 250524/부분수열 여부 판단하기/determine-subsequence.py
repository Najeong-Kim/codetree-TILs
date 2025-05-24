n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ai = 0
count = 0

for i in range(m):
    while ai + 1 < n and A[ai] != B[i]:
        ai += 1
    if ai < n and A[ai] == B[i]:
        count += 1
        ai += 1

if count == len(B):
    print('Yes')
else:
    print('No')