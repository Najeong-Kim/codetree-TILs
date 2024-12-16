N = int(input())
arr = list(input())

result = 0
is_empty = False
now = 0

for i in range(N):
    if arr[i] == '0':
        is_empty = True
        now += 1
    elif arr[i] == '1':
        is_empty = False
        if now % 2 == 0:
            result = max(result, now // 2)
        else:
            result = max(result, now // 2 + 1)
        now = 0

result = max(result, now)

print(result)