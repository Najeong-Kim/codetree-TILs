N = int(input())
arr = [0] * 1001
times = []

max_ot = 0

for _ in range(N):
    A, B = map(int, input().split())
    times.append([A, B])
    for i in range(A, B):
        arr[i] += 1

for i in range(N):
    copy_arr = arr[:]
    for j in range(times[i][0], times[i][1]):
        copy_arr[j] -= 1
    ot = 0
    for elem in copy_arr:
        if elem:
            ot += 1
    max_ot = max(max_ot, ot)

print(max_ot)
