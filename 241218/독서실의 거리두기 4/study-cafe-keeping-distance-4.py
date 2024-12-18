N = int(input())
arr = list(input())

result = 0

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] == '1' or arr[j] == '1':
            continue
        arr[i] = '1'
        arr[j] = '1'

        cur = []
        for k in range(N):
            if arr[k] == '1':
                cur.append(k)

        distance = 100

        for k in range(len(cur)-1):
            distance = min(distance, cur[k+1] - cur[k])
        
        result = max(result, distance)

        arr[i] = '0'
        arr[j] = '0'

print(result)