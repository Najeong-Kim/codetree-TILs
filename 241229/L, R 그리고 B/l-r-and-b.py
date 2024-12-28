L = None
R = None
B = None

for i in range(10):
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] != '.':
            if arr[j] == 'L':
                L = [i, j]
            elif arr[j] == 'R':
                R = [i, j]
            elif arr[j] == 'B':
                B = [i, j]
if L[0] != B[0] and L[1] != B[1]:
    print(abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1)
else:
    if L[0] == B[0] == R[0] and (L[1] < R[1] < B[1] or L[1] > R[1] > B[1]):
        print(abs(B[1] - L[1]) + 1)
    elif L[1] == B[1] == R[1] and (L[0] < R[0] < B[0] or L[0] > R[0] > B[0]):
        print(abs(B[0] - L[0]) + 1)
    else:
        print(abs(B[0] - L[0]) + abs(B[1] - L[1]) - 1)