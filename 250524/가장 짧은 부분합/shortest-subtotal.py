n, s = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
result = 10 ** 9
current = arr[0]

for start in range(n):
    while current < s:
        end += 1
        if end >= n:
            break
        current += arr[end]
    if current >= s and end < n:
        result = min(result, end - start + 1)
        current -= arr[start]

if result == 10 ** 9:
    print(-1)
else:
    print(result)