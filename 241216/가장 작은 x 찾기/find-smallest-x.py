n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(10001):
    is_possible = True
    for j in range(n):
        if arr[j][0] <= (i * (2 ** (j + 1))) <= arr[j][1]:
            continue
        else:
            is_possible = False
            break
    if is_possible:
        print(i)
        break
