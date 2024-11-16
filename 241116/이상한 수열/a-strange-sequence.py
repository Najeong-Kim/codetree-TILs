def function(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return function(n // 3) + function(n - 1)

N = int(input())
print(function(N))