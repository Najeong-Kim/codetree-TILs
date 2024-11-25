n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_num = 0
cnt = 0
for i in range(n):
    if arr[i] <= t:
        max_num = max(max_num, cnt)
        cnt = 0
    else:
        cnt += 1

max_num = max(max_num, cnt)

print(max_num)