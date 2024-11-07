def getGCD(n, m):
    gcd = 1
    for i in range(1, 101):
        if (n % i == 0 and m % i == 0):
            gcd = i
    return gcd

n, m = map(int, input().split())
print(getGCD(n, m))