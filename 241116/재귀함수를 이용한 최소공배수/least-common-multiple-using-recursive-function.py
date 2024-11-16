n = int(input())
arr = list(map(int, input().split()))

def LCM(a, b):
    n = a
    while (n % a != 0 or n % b != 0):
        n += 1
    return n

def function(n):
    if n == len(arr):
        return n
    return LCM(arr[n], function(n + 1))

print(function(arr[0]))
