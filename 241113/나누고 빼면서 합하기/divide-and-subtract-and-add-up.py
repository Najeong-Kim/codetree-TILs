n, m = map(int, input().split())
A = list(map(int, input().split()))
total = 0

def function(m, A):
    global total
    while m > 1:
        total += A[m - 1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    total += A[0]

function(m, A)
print(total)
