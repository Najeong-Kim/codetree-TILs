from sortedcontainers import SortedSet 

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = SortedSet()
s.add((-(n + 1), -1, n + 1))

for num in nums:
    for elem in s:
        if elem[1] < num < elem[2]:
            s.add((-(num - elem[1] - 1), elem[1], num))
            s.add((-(elem[2] - num - 1), num, elem[2]))
            s.remove(elem)
    print(-s[0][0])
