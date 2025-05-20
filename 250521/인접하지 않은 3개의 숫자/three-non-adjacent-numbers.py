n = int(input())
arr = list(map(int, input().split()))

front = [0] * n
front[0] = arr[0]
back = [0] * n
back[-1] = arr[-1]

for i in range(1, n):
    front[i] = max(front[i - 1], arr[i])

for i in range(n - 2, -1, -1):
    back[i] = max(back[i + 1], arr[i])

result = 0
for i in range(2, n - 2):
    result = max(result, front[i - 2] + arr[i] + back[i + 2])

print(result)