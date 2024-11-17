n = int(input())
arr = []

for i in range(1, n + 1):
    h, w = input().split()
    arr.append((h, w, i))

arr.sort(key=lambda x: (-int(x[0]), -int(x[1]), x[2]))

for elem in arr:
    h, w, i = elem
    print(h, w, i)