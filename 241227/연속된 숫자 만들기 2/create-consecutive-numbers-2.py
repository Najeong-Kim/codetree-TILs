a, b, c = map(int, input().split())

arr = sorted([a, b, c])

if arr[1] - arr[0] == 1 and arr[2] - arr[1] == 1:
    print(0)
elif arr[1] - arr[0] == 1 or arr[2] - arr[1] == 1:
    print(1)
else:
    print(2)