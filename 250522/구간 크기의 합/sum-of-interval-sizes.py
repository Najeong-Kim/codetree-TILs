n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

arr = []
for i in intervals:
    arr.append((i[0], 1))
    arr.append((i[1], -1))

arr.sort()

start = arr[0][0]
is_connected = True
count = 0
result = 0

for i in range(len(arr)):
    point, value = arr[i]
    count += value
    if not is_connected:
        start = point
        is_connected = True
    if count == 0:
        result += point - start
        is_connected = False

print(result)