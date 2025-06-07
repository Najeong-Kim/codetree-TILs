n = int(input())

left = 1
right = 10 ** 18
min_value = 10 ** 18

while left <= right:
    mid = (left + right) // 2
    count = mid - (mid // 3) - (mid // 5) + (mid // 15)
    if count == n:
        min_value = min(min_value, mid)
        right = mid - 1
    elif count < n:
        left = mid + 1
    else:
        right = mid - 1

print(min_value)