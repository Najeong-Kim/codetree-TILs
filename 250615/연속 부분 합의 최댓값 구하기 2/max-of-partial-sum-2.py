n = int(input())
a = list(map(int, input().split()))

result = a[0]
now = 0
for i in range(len(a)):
    if now < 0:
        now = a[i]
    else:
        now += a[i]
    result = max(result, now)

print(result)