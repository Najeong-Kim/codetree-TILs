from sortedcontainers import SortedSet 

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = SortedSet()
s.add((-(n + 1), -1, n + 1))
intervals = SortedSet()
intervals.add((-1, n + 1))

for num in nums:
    interval = intervals.bisect_right((num, n + 1)) - 1
    a, b = intervals[interval]
    s.add((-(num - a - 1), a, num))
    s.add((-(b - num - 1), num, b))
    s.remove((-(b - a - 1), a, b))
    
    if a < num - 1:
        intervals.add((a, num))
    if num + 1 < b:
        intervals.add((num, b))
    intervals.remove((a, b))
    
    print(-s[0][0])
