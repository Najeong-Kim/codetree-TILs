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
    if A[i] in da:
        da[A[i]] += 1
    else:
        da[A[i]] = 1
    if B[i] in db:
        db[B[i]] += 1
    else:
        db[B[i]] = 1
    if C[i] in dc:
        dc[C[i]] += 1
    else:
        dc[C[i]] = 1
    if D[i] in dd:
        dd[D[i]] += 1
    else:
        dd[D[i]] = 1

dab = {}
dcd = {}
for a in da:
    for b in db:
        if a + b in dab:
            dab[a + b] += da[a] * db[b]
        else:
            dab[a + b] = da[a] * db[b]

for c in dc:
    for d in dd:
        if c + d in dcd:
            dcd[c + d] += dc[c] * dd[d]
        else:
            dcd[c + d] = dc[c] * dd[d]

count = 0
for ab in dab:
    if -ab in dcd:
        count += dab[ab] * dcd[-ab]

print(count)