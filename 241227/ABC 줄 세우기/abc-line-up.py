n = int(input())
order='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = list(input().split())

count = 0
index = 0

while index != n - 1:
    alphabet = order[index]
    now = arr.index(alphabet)
    if index != now:
        for i in reversed(range(index + 1, now + 1)):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            count += 1
    index += 1

print(count)
