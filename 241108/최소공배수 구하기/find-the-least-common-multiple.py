def getLCM(n, m):
    lcm = 1
    while True:
        if lcm % n == 0 and lcm % m == 0:
            return lcm
        else:
            lcm += 1

n, m = map(int, input().split())
print(getLCM(n, m))