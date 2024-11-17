n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

arr.sort(key=lambda x: int(x[1]) + int(x[2]) + int(x[3]))

for elem in arr:
    print(" ".join(elem))