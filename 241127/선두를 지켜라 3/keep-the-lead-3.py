N, M = map(int, input().split())

A = [0]
B = [0]

def record_moving(n, arr):
    for _ in range(n):
        v, t = map(int, input().split())
        for _ in range(t):
            arr.append(arr[-1] + v)

record_moving(N, A)
record_moving(M, B)

is_changed = 0
leader = ""

for i in range(1,len(A)):
    if not len(leader) and A[i] != B[i]:
        is_changed += 1
        leader = "A" if A[i] > B[i] else "B"
    elif len(leader) and A[i] == B[i]:
        is_changed += 1
        leader = ""
    elif leader == "B" and A[i] > B[i]:
        is_changed += 1
        leader = "A"
    elif leader == "A" and A[i] < B[i]:
        is_changed += 1
        leader = "B"

print(is_changed)   
