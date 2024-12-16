N = int(input())
arr = list(input())

result = 0

for i in range(N):
    if arr[i] == '1':
        continue
    arr[i] = '1'

    cur = []
    for j in range(N):
        if arr[j] == '1':
            cur.append(j)

    distance = 20

    for j in range(len(cur)-1):
        distance = min(distance, cur[j+1] - cur[j])
    
    result = max(result, distance)

    arr[i] = '0'

print(result)