def function(n):
    if n <= 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (function(n - 1) * function(n - 2)) % 100

N = int(input())
print(function(N))