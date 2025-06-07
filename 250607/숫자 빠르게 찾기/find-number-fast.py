n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

def binary_search(target):
    left, right = 0, n - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            idx = mid
            break
        
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return idx

for query in queries:
    idx = binary_search(query)
    if idx == -1:
        print(idx)
    else:
        print(idx + 1)
