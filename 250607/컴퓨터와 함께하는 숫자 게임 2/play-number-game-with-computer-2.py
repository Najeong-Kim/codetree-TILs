m = int(input())
a, b = map(int, input().split())
min_count = 10 ** 9
max_count = 0

def binary_search(target):
    left, right = 1, m
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1
        if mid == target:
            break
        elif mid > target:
            right = mid - 1
        else:
            left = mid + 1
    return count

for i in range(a, b + 1):
    count = binary_search(i)
    min_count = min(min_count, count)
    max_count = max(max_count, count)

print(min_count, max_count)
