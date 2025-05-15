n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix_sum = [0]
for elem in arr:
    prefix_sum.append(prefix_sum[-1] + elem)

result = 0
for i in range(n):
    for j in range(n - i + 1):
        if prefix_sum[j + i] - prefix_sum[j] == k:
            result += 1

print(result)