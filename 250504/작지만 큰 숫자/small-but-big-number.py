from sortedcontainers import SortedSet

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
s = SortedSet()
for i in range(n):
    s.add(sequence[i])

for i in query:
    index = s.bisect_right(i)
    if not len(s) or index == 0:
        print(-1)
        continue
    print(s[index - 1])
    s.remove(s[index - 1])