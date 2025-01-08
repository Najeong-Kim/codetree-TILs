n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp = l[-1]
    temp2 = r[-1]
    temp3 = d[-1]
    for i in reversed(range(n - 1)):
        l[i + 1] = l[i]
        r[i + 1] = r[i]
        d[i + 1] = d[i]
    l[0] = temp3
    r[0] = temp
    d[0] = temp2

for i in l:
    print(i, end=' ')
print()
for i in r:
    print(i, end=' ')
print()
for i in d:
    print(i, end=' ')