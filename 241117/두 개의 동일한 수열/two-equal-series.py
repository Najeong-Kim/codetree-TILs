n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def is_identical(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return 'No'
    return 'Yes'

print(is_identical(A, B))