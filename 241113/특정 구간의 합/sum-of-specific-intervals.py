n, m = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(m):
    a_1, a_2 = map(int, input().split())
    total = 0
    for i in range(a_1 - 1, a_2):
        total += A[i]
    print(total)