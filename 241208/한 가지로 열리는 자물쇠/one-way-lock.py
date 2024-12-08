N = int(input())
a, b, c = map(int, input().split())

total = N * N * N

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if abs(a - i) > 2 and abs(b - j) > 2 and abs(c - k) > 2:
                total -= 1

print(total)
