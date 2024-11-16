def recursive_function(n):
    if n == 0 or n == 1:
        return n
    return n + recursive_function(n - 2)

N = int(input())
print(recursive_function(N))