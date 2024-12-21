n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(sum(arr)):
    count = 0
    current = 0
    is_possible = True
    for j in range(len(arr)):
        if current + arr[j] <= i:
            current += arr[j]
        else:
            if arr[j] > i:
                is_possible = False
            else:
                count += 1
                current = arr[j]
    if count < m and is_possible:
        print(i)
        break
