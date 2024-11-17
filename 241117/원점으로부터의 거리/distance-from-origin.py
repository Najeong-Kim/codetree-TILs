n = int(input())
arr = []

for i in range(1, n + 1):
    x, y = map(int, input().split())
    arr.append((x, y, i))

arr.sort(key=lambda x: (abs(x[0]) + abs(x[1]), x[2]))

for elem in arr:
    _, _, i = elem
    print(i)
