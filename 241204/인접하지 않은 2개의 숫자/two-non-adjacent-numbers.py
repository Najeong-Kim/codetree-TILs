n = int(input())
arr = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            max_sum = max(max_sum, arr[i] + arr[k])

print(max_sum)