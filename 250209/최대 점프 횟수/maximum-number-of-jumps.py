n = int(input())
arr = list(map(int, input().split()))
result = [-1] * n
result[0] = 0

for i in range(n):
    if result[i] == -1:
        continue
    for j in range(i + 1, min(n, i + 1 + arr[i])):
        result[j] = max(result[j], result[i] + 1)

print(max(result))