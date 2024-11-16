n = int(input())
arr = list(map(int, input().split()))

def LCM(n):
    if all(n % a == 0 for a in arr):
        return n
    return LCM(n + 1)

print(LCM(1))
