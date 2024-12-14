N = int(input())
arr = [int(input()) for _ in range(N)]

result = 0

for i in range(max(arr)):
    is_submerged = False
    count = 0
    for j in range(N):
        if arr[j] > i:
            if not is_submerged:
                is_submerged = True
                count += 1
        else:
            if is_submerged:
                is_submerged = False
    result = max(result, count)

print(result)
    
