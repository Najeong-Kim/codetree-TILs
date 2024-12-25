n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = [(A[i] - B[i]) for i in range(n)]

total = 0

def findIndex(func, arr):
    for i, v in enumerate(arr):
        if func(v):
            return i

for i in range(len(arr)):
    while True:
        if arr[i] == 0:
            break
        j = findIndex(lambda x: x < 0, arr)
        start = arr[i]
        end = arr[j]
        move = min(start, abs(end))
        total += move * (j - i)
        arr[i] -= move
        arr[j] += move

print(total)
