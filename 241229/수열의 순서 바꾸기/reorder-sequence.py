N = int(input())
arr = list(map(int, input().split()))

result = 0

for i in range(len(arr) - 1):
    now = len(arr) - 1 - i
    if arr[now] < arr[now - 1]:
        result = now
        break

print(result)