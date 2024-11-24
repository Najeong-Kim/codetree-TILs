N = int(input())
arr = [int(input()) for _ in range(N)]

max_num = 0
cnt = 0
for i in range(N):
    if i == 0 or (arr[i] * arr[i - 1] < 0):
        max_num = max(max_num, cnt)
        cnt = 1
    else:
        cnt += 1

max_num = max(max_num, cnt)

print(max_num)