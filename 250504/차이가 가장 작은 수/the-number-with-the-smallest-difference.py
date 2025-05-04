from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
s = SortedSet([arr[0]])
diff = 10 ** 9 + 10
for i in range(1, n):
    s.add(arr[i])
    index = s.bisect_left(arr[i])
    if index > 0:
        current_diff = abs(arr[i] - s[index - 1])
        if current_diff >= m:
            diff = min(diff, current_diff)
    if index < len(s) - 1:
        current_diff = abs(arr[i] - s[index + 1])
        if current_diff >= m:
            diff = min(diff, current_diff)

if diff == (10 ** 9 + 10):
    print(-1)
else:
    print(diff)
