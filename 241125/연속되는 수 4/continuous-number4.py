N = int(input())
arr = [int(input()) for _ in range(N)]

max_num = 0
cnt = 1
prev = arr[0]
for i in range(1, N):
    if arr[i] <= prev:
        max_num = max(max_num, cnt)
        prev = arr[i]
        cnt = 1
    else:
        prev = arr[i]
        cnt += 1


max_num = max(max_num, cnt)

print(max_num)