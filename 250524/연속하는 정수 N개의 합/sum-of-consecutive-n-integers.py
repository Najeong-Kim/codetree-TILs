n, m = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
result = 0
current = arr[0]

for start in range(n):
    while current < m and end + 1 < n:
        end += 1
        current += arr[end]
    if current == m and end < n:
        result += 1
    current -= arr[start]

print(result)