N = int(input())
arr = [int(input()) for _ in range(N)]

max_num = 0
cnt = 0
prev = 0
for i in range(N):
    if i == 0 or (arr[i] <= prev):
        max_num = max(max_num, cnt)
        prev = 0
        cnt = 1
    else:
        prev = arr[i]
        cnt += 1


max_num = max(max_num, cnt)

print(max_num)