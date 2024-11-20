n = int(input())
arr = [0] * (200 + 1)

for _ in range(n):
    A, B = map(int, input().split())
    for i in range(A + 100, B + 100):
        arr[i] += 1

print(max(arr))