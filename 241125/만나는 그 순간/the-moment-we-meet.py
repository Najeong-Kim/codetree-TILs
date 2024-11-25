N, M = map(int, input().split())

A = [0]
B = [0]

def record_moving(n, arr):
    for _ in range(n):
        direction, count = input().split()
        if direction == 'R':
            for i in range(int(count)):
                arr.append(arr[-1] + 1)
        else:
            for i in range(int(count)):
                arr.append(arr[-1] - 1)

record_moving(N, A)
record_moving(M, B)

is_meet = False

for i in range(1, len(A)):
    if A[i] == B[i]:
        print(i)
        is_meet = True
        break

if not is_meet:
    print(-1)        
