n = int(input())
arr = [0] * (100 + 1)

for _ in range(n):
    A, B = map(int, input().split())
    for i in range(A, B + 1):
        arr[i] += 1

print(max(arr))