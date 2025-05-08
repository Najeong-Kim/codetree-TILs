n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
count = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            SA = set()
            SB = set()
            for x in range(n):
                SA.add(A[x][i] + A[x][j] + A[x][k])
                SB.add(B[x][i] + B[x][j] + B[x][k])
            if not len(SA.intersection(SB)):
                count += 1

print(count)
