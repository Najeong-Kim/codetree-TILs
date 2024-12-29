arr = list(map(int, input().split()))
arr.sort()

A = arr[0]
B = arr[1]
C = arr[2] if A + B != arr[2] else arr[3]

print(A, B, C)
