n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    now = i
    time = 1
    value = arr[now - 1]
    while time < m:
        now = arr[now - 1]
        value += arr[now - 1]
        time += 1
    max_sum = max(max_sum, value)

print(max_sum)