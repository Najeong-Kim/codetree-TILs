from sortedcontainers import SortedSet

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = SortedSet()

for i in range(1, m + 1):
    s.add(i)

result = 0
for i in range(n):
    seat_index = s.bisect_right(a[i])
    if seat_index == 0:
        break
    s.remove(s[seat_index - 1])
    result += 1

print(result)