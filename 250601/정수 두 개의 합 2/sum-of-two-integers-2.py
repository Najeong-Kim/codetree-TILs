n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
start = 0
end = n - 1
count = 0

while start != end:
    if arr[start] + arr[end] <= k:
        count += end - start
        start += 1
    else:
        
        end -= 1

print(count)