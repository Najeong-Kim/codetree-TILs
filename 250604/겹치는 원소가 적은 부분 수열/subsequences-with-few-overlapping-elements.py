n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0

dict = {}

dict[arr[start]] = 1
count = 1
result = 1

while end != n - 1:
    if arr[end + 1] in dict and dict[arr[end + 1]] >= k:
        if start == end:
            dict[arr[start]] -= 1
            start += 1
            end += 1
            dict[arr[end]] += 1
        else:
            dict[arr[start]] -= 1
            start += 1
            count -= 1
    else:
        end += 1
        if arr[end] in dict:
            dict[arr[end]] += 1
        else:
            dict[arr[end]] = 1
        count += 1
    result = max(result, count)

print(result)
