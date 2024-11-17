n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr.sort()

for elem in arr:
    print(elem)