N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(N):
    copy_arr = arr[:]
    del copy_arr[i]

    x1, x2 = arr[i]
    ok = True
    for elem in copy_arr:
        if x1 > elem[0] and x2 < elem[1]:
            ok = False
            break
        elif x1 < elem[0] and x2 > elem[1]:
            ok = False
            break
    if ok:
        count += 1

print(count)