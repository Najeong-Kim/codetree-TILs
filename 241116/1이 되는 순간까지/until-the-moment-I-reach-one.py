def until_1(n, m):
    if n == 1:
        return m
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    return until_1(n, m + 1)

N = int(input())
print(until_1(N, 0))