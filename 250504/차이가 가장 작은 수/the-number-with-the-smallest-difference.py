from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
s = SortedSet()
diff = 10 ** 10
for i in range(n):
    s.add(arr[i])

si = 0
ei = 1
while si != len(s) and ei != len(s):
    start, end = s[si], s[ei]
    if end - start >= m:
        diff = min(diff, end - start)
        si += 1
    else:
        ei += 1

if diff == (10 ** 10):
    print(-1)
else:
    print(diff)
