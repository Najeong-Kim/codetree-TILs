n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
da = {}
db = {}
dc = {}
dd = {}
for i in range(n):
    da[A[i]] = True
    db[B[i]] = True
    dc[C[i]] = True
    dd[D[i]] = True

dab = {}
dcd = {}
for a in da:
    for b in db:
        if a + b in dab:
            dab[a + b] += 1
        else:
            dab[a + b] = 1

for c in dc:
    for d in dd:
        if c + d in dcd:
            dcd[c + d] += 1
        else:
            dcd[c + d] = 1

count = 0
for ab in dab:
    if -ab in dcd:
        count += dab[ab] * dcd[-ab]

print(count)