N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def function(arr):
    result = arr[0] + arr[-1]
    for i in range(len(arr)//2):
        result = max(result, arr[i] + arr[len(arr) - 1 - i])
    return result

print(function(arr))