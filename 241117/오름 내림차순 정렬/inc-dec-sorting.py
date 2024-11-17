n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in arr:
    print(i, end=" ")

print("")

arr2 = reversed(arr)

for i in arr2:
    print(i, end=" ")