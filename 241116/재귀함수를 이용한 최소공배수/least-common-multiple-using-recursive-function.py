n = int(input())
arr = list(map(int, input().split()))

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return int(a * b / GCD(a, b))

def function(n):
    if n == len(arr) - 1:
        return arr[n]
    return LCM(arr[n], function(n + 1))

print(function(arr[0]))
