n = int(input())
arr = []

for i in range(1, n + 1):
    x, y = map(int, input().split())
    arr.append((x, y, i))

arr.sort(key=lambda x: (x[0], -x[1], x[2]))

for elem in arr:
    h, w, i = elem
    print(h, w, i)
