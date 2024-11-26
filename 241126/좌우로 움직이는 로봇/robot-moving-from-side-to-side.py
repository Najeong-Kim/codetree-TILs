N, M = map(int, input().split())

A = [0]
B = [0]

def record_moving(n, arr):
    for _ in range(n):
        t, d = input().split()
        if d == 'R':
            for i in range(int(t)):
                arr.append(arr[-1] + 1)
        else:
            for i in range(int(t)):
                arr.append(arr[-1] - 1)

record_moving(N, A)
record_moving(M, B)

result = 0
is_meet = True

for i in range(1, max(len(A), len(B))):
    A_index = min(i, len(A) - 1)
    B_index = min(i, len(B) - 1)
    if A[A_index] == B[B_index]:
        if not is_meet:
            result += 1
            is_meet = True
    else:
        is_meet = False

print(result)