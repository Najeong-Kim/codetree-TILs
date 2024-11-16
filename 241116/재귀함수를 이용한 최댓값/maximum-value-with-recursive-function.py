def maximum_value(arr, n):
    if len(arr) - 1 == n:
        return arr[n]
    return max(maximum_value(arr, n + 1), arr[n])
    

n = int(input())
arr = list(map(int, input().split()))

print(maximum_value(arr, 0))