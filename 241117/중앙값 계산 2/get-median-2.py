n = int(input())
arr = list(map(int, input().split()))

def median_calculation(n):
    if n == 1:
        return str(arr[0])
    return median_calculation(n - 2) + ' ' + str(sorted(arr[:n])[n//2])

print(median_calculation(n))