N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N):
    current = []
    for j in range(N):
        if i == j:
            current.append(arr[j][0] // 2 + arr[j][1])
        else:
            current.append(sum(arr[j]))
    current.sort()
    budget = 0
    count = 0
    for k in range(len(current)):
        if budget + current[k] <= B:
            budget += current[k]
            count += 1
        else:
            break
    result = max(count, result)

print(result)