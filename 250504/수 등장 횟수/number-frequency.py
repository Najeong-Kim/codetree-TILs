n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

dict = {}
for i in range(n):
    if arr[i] in dict:
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

for i in range(m):
    if nums[i] in dict:
        print(dict[nums[i]], end=' ')
    else:
        print(0, end=' ')