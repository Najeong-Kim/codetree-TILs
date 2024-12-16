n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(arr[0][0], arr[0][1] + 1):
    is_possible = True
    for j in range(n):
        if arr[j][0] <= i * (2 ** (j + 1)) <= arr[j][1]:
            continue
        else:
            is_possible = False
            break
    if is_possible:
        print(i)
        break
