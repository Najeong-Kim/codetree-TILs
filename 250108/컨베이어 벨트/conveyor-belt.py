n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp = u[-1]
    temp2 = d[-1]
    for i in reversed(range(n - 1)):
        u[i + 1] = u[i]
        d[i + 1] = d[i]
    u[0] = temp2
    d[0] = temp

for i in u:
    print(i, end=' ')
print()
for i in d:
    print(i, end=' ')