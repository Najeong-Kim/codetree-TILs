n = 5
arr = []

for i in range(n):
    arr.append(input().split())

arr.sort(key=lambda x: x[0])

print('name')
for elem in arr:
    name, height, weight = elem
    print(name, height, weight)

print('')

arr.sort(key=lambda x: -int(x[1]))

print('height')
for elem in arr:
    name, height, weight = elem
    print(name, height, weight)