def function(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return function(n // 2) + 1
    else:
        return function(n * 3 + 1) + 1

n = int(input())
print(function(n))