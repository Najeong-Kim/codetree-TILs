s = int(input())

def binary_search(target):
    left = 1
    right = 10 ** 18
    max_num = 0

    while left <= right:
        mid = (left + right) // 2
        if (mid * (mid + 1)) / 2 <= target:
            max_num = max(max_num, mid)
            left = mid + 1
        else:
            right = mid - 1
    return max_num

print(binary_search(s))