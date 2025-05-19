from sortedcontainers import SortedSet 

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = SortedSet()

for num in nums:
    count = 0
    s.add(num)
    for i in range(len(s) - 1):
        count = max(count, s[i + 1] - s[i] - 1)
    count = max(count, n - s[-1], s[0])
    print(count)
