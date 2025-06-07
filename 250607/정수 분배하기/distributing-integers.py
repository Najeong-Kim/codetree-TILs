n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_value = 0
left = 1
right = 100000

while left <= right:
    mid = (left + right) // 2
    count = 0
    for elem in arr:
        count += elem // mid
    if count >= m:
        left = mid + 1
        max_value = max(max_value, mid)
    else:
        right = mid - 1

print(max_value)