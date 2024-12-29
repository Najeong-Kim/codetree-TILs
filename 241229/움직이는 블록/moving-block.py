N = int(input())
arr = [int(input()) for _ in range(N)]
block = sum(arr) // len(arr)

count = 0
for elem in arr:
    count += abs(block - elem)

print(count // 2)
