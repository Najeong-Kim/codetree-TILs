n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

arr.sort(key=lambda x: (int(x[1]), -int(x[2]), x[0]))

for elem in arr:
    name, height, weight = elem
    print(name, height, weight)
