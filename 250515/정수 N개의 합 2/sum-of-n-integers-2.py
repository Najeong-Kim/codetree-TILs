n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix_sum = [0]
for elem in arr:
    prefix_sum.append(prefix_sum[-1] + elem)

result = - 10 ** 9
for i in range(n - k + 1):
    result = max(result, prefix_sum[i + k] - prefix_sum[i])

print(result)