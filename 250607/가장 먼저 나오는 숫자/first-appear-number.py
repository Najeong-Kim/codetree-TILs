n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for q in query:
    lower = lower_bound(q)
    if lower == n:
        print(-1)
    else:
        print(lower + 1)