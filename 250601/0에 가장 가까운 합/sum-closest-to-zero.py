n = int(input())
a = list(map(int, input().split()))

a.sort()
left = 0
right = n - 1
result = 10 ** 10

while left != right:
    total = a[left] + a[right]
    result = min(result, abs(total))

    if total > 0:
        right -= 1
    else:
        left += 1

print(result)