n = int(input())
nums = [1, 2, 5]
arr = [0] * (n + 1)

for num in nums:
    arr[num] = 1

for i in range(n + 1):
    for num in nums:
        if i - num < 0:
            continue
        arr[i] = (arr[i] + arr[i - num]) % 10007

print(arr[n])
